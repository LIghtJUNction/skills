#!/usr/bin/env python3
"""Build a public skill index from GitHub metadata; never execute skill content."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
OWNER = "LIghtJUNction"
DATA = ROOT / "data/catalog.json"


def api(endpoint):
    result = subprocess.run(
        ["gh", "api", endpoint], capture_output=True, text=True, timeout=90
    )
    if result.returncode:
        raise RuntimeError(f"GitHub request failed: {endpoint}\n{result.stderr}")
    return json.loads(result.stdout)


def discover():
    repos = []
    page = 1
    while True:
        batch = api(f"users/{OWNER}/repos?per_page=100&type=owner&page={page}")
        repos.extend(r for r in batch if not r["fork"] and not r["private"]
                     and r["name"] != "skills")
        if len(batch) < 100:
            break
        page += 1

    def scan(repo):
        branch = repo["default_branch"]
        tree = api(f"repos/{repo['full_name']}/git/trees/{quote(branch, safe='')}?recursive=1")
        if tree.get("truncated"):
            raise RuntimeError(f"Incomplete tree: {repo['full_name']}")
        paths = sorted(item["path"] for item in tree["tree"]
                       if item["type"] == "blob"
                       and item["path"].split("/")[-1] == "SKILL.md")
        return dict(repo=repo["full_name"], branch=branch,
                    description=repo["description"], archived=repo["archived"],
                    sha=tree["sha"], paths=paths, truncated=False)

    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(scan, repos))
    return dict(owner=OWNER, checked_at=datetime.now(timezone.utc).isoformat(),
                repositories=sorted(results, key=lambda r: r["repo"].lower()))


def validate(data):
    assert data["owner"] == OWNER
    datetime.fromisoformat(data["checked_at"])
    seen = set()
    for repo in data["repositories"]:
        name = repo["repo"]
        assert name.startswith(OWNER + "/") and name not in seen, name
        seen.add(name)
        assert not repo.get("error") and not repo.get("truncated"), name
        assert repo["sha"] is None or re.fullmatch(r"[0-9a-f]{40}", repo["sha"]), name
        assert isinstance(repo["archived"], bool)
        assert len(repo["paths"]) == len(set(repo["paths"])), name
        for path in repo["paths"]:
            assert path.split("/")[-1] == "SKILL.md", path
            assert not path.startswith("/") and ".." not in path.split("/"), path
            assert repo["sha"], name


def url(repo, path, pinned=False):
    ref = repo["sha"] if pinned else repo["branch"]
    return f"https://github.com/{repo['repo']}/blob/{quote(ref, safe='')}/{quote(path, safe='/')}"


def cell(value):
    return str(value).replace("|", "&#124;").replace("\n", " ")


def replace_section(text, name, content):
    start, end = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    assert text.count(start) == text.count(end) == 1, name
    before, rest = text.split(start)
    _, after = rest.split(end)
    return before + start + "\n" + content + "\n" + end + after


def outputs(data):
    validate(data)
    repos = data["repositories"]
    found = [r for r in repos if r["paths"]]
    count = sum(len(r["paths"]) for r in found)
    date = data["checked_at"][:10]
    stats = (f"截至 {date}（UTC），检查了 **{len(repos)}** 个公开非 Fork 仓库，"
             f"其中 **{len(found)}** 个仓库有技能，共 **{count}** 个 `SKILL.md` 文件入口。"
             "这是文件入口数量，未按名称或内容去重。汇总仓库本身不计入扫描。")
    by_name = {r["repo"].split("/")[-1]: r for r in repos}
    highlights = json.loads((ROOT / "data/highlights.json").read_text())
    sections = []
    for group in highlights:
        sections.extend([f"### {group['title']}", "", "| 技能 | 用来做什么 |", "| --- | --- |"])
        for item in group["items"]:
            repo = by_name[item["repo"]]
            path = item["path"]
            assert path in repo["paths"], (item["repo"], path)
            status = "（已归档）" if repo["archived"] else ""
            sections.append(f"| [{cell(item['name'])}]({url(repo, path)}){status} | {cell(item['description'])} |")
        sections.append("")
    readme = (ROOT / "README.md").read_text()
    readme = replace_section(readme, "highlights", "\n".join(sections).rstrip())
    readme = replace_section(readme, "stats", stats)
    lines = ["# 完整技能目录", "", "[返回首页](README.md)", "", stats, "",
             "按来源仓库排列；同名入口保留各自路径。技能名称取自目录名，根目录技能用仓库名表示，未解析 frontmatter。",
             "快照链接固定到本次核对的提交。项目随附技能可能来自第三方，归属与许可请看原仓库。", ""]
    for archived, title in [(False, "未归档仓库"), (True, "已归档仓库")]:
        lines.extend([f"## {title}", ""])
        for repo in found:
            if repo["archived"] != archived:
                continue
            lines.extend([f"### [{repo['repo']}](https://github.com/{repo['repo']})", "",
                          "| 技能入口 | 仓库内路径 | 核对快照 |", "| --- | --- | --- |"])
            for path in repo["paths"]:
                name = path.split("/")[-2] if "/" in path else repo["repo"].split("/")[-1]
                lines.append(f"| [{cell(name)}]({url(repo, path)}) | `{path}` | [固定版本]({url(repo, path, True)}) |")
            lines.append("")
    return {ROOT / "README.md": readme, ROOT / "CATALOG.md": "\n".join(lines)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["refresh", "render", "check"])
    args = parser.parse_args()
    data = discover() if args.command == "refresh" else json.loads(DATA.read_text())
    rendered = outputs(data)
    if args.command == "check":
        for path, expected in rendered.items():
            if not path.exists() or path.read_text() != expected:
                raise SystemExit(f"Out of date: {path.name}; run render")
        print("OK: catalog structure, unique paths, highlight sources and generated documents")
        return
    if args.command == "refresh":
        DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    for path, content in rendered.items():
        path.write_text(content)
    print(f"Updated {len(rendered)} documents")


if __name__ == "__main__":
    main()
