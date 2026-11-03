# 我的 Agent 技能

我发布在 GitHub 上的技能，放在这里方便找。做图、写代码、查资料、折腾 Linux，还有《缺氧》。

这里是目录。技能文件、脚本和示例留在各自仓库，点链接就能看。

## 从这里找

<!-- highlights:start -->
### 做图和写内容

#### [draw-project-meme](https://github.com/LIghtJUNction/draw-project-meme/blob/main/SKILL.md)

查清开源项目的原理，再画成荒诞手绘梗图。

```sh
npx skills add LIghtJUNction/draw-project-meme
```

#### [anime-reaction-gif](https://github.com/LIghtJUNction/anime-reaction-gif/blob/main/skills/anime-reaction-gif/SKILL.md)

用角色姿势图做循环表情 GIF，附 MP4 预览。

```sh
npx skills add https://github.com/LIghtJUNction/anime-reaction-gif/tree/main/skills/anime-reaction-gif
```

#### [ascii-morph-gif](https://github.com/LIghtJUNction/ascii-morph-gif/blob/main/skills/ascii-morph-gif/SKILL.md)

让一个物体变成另一个物体，做成 ASCII 字符动画。

```sh
npx skills add https://github.com/LIghtJUNction/ascii-morph-gif/tree/main/skills/ascii-morph-gif
```

#### [painterly-loop-gif](https://github.com/LIghtJUNction/painterly-loop-gif/blob/main/skills/painterly-loop-gif/SKILL.md)

做带雨滴、萤火虫和轻微摇摆的绘画风循环 GIF。

```sh
npx skills add https://github.com/LIghtJUNction/painterly-loop-gif/tree/main/skills/painterly-loop-gif
```

#### [particle-sculpture](https://github.com/LIghtJUNction/particle-sculpture-skill/blob/main/SKILL.md)

做可交互的 3D 粒子雕塑，包含动画和鼠标、触摸响应。

```sh
npx skills add LIghtJUNction/particle-sculpture-skill
```

#### [二手车短视频文案](https://github.com/LIghtJUNction/used-car-video-copywriting-skill/blob/main/.agents/skills/douyin-used-car-video-copy/SKILL.md)

根据真实车辆信息写口播、分镜和拍摄素材清单。

```sh
npx skills add https://github.com/LIghtJUNction/used-car-video-copywriting-skill/tree/main/.agents/skills/douyin-used-car-video-copy
```


### 开发和项目推广

#### [geg](https://github.com/LIghtJUNction/geg/blob/main/skills/geg/SKILL.md)

用语义搜索查本地代码和文本。

```sh
npx skills add https://github.com/LIghtJUNction/geg/tree/main/skills/geg
```

#### [cpyref](https://github.com/LIghtJUNction/cpyref/blob/main/skills/cpyref/SKILL.md)

通过引用交接笔记和文件，按需读取并复用原始字节。

```sh
npx skills add https://github.com/LIghtJUNction/cpyref/tree/main/skills/cpyref
```

#### [markref](https://github.com/LIghtJUNction/markref/blob/main/skills/markref/SKILL.md)

定位分散在多个文件里的同一功能，维护源码标记。

```sh
npx skills add https://github.com/LIghtJUNction/markref/tree/main/skills/markref
```

#### [awesome-submit](https://github.com/LIghtJUNction/awesome-submit/blob/main/SKILL.md)

检查收录规则和重复项，把项目提交到合适的 awesome 列表。

```sh
npx skills add LIghtJUNction/awesome-submit
```

#### [x-quality-growth](https://github.com/LIghtJUNction/x-quality-growth/blob/main/SKILL.md)

结合 X 开源推荐算法做内容和互动实验，记录结果。

```sh
npx skills add LIghtJUNction/x-quality-growth
```


### Linux 和缺氧

#### [linux-windows-apps](https://github.com/LIghtJUNction/linux-windows-apps/blob/main/SKILL.md)

在 Linux 上通过 Wine 或 Bottles 安装和运行 Windows 应用。

```sh
npx skills add LIghtJUNction/linux-windows-apps
```

#### [agentic-bees](https://github.com/LIghtJUNction/agentic-bees/blob/main/skills/agentic-bees/SKILL.md)

按限定范围扫描 Btrfs 重复数据，再执行授权的去重。

```sh
npx skills add https://github.com/LIghtJUNction/agentic-bees/tree/main/skills/agentic-bees
```

#### [mechrevo-verification](https://github.com/LIghtJUNction/mechrevo-drivers/blob/main/docs/skills/mechrevo-verification/SKILL.md)

核验机械革命 Linux 驱动的构建、安装和硬件表现。

```sh
npx skills add https://github.com/LIghtJUNction/mechrevo-drivers/tree/main/docs/skills/mechrevo-verification
```

#### [oni-skills](https://github.com/LIghtJUNction/oni-skills/blob/main/SKILL.md)

查《缺氧》的游戏机制、工程方案和阶段决策。

```sh
npx skills add LIghtJUNction/oni-skills
```


### 已归档

#### [software2prompt](https://github.com/LIghtJUNction/software2prompt/blob/main/SKILL.md)（已归档）

从源码、二进制或运行实例提取软件重建提示词，并设计对比验证。

```sh
npx skills add LIghtJUNction/software2prompt
```
<!-- highlights:end -->

## 怎么用

上面每个技能都有独立的安装命令，代码块右上角可以直接复制。需要 Node.js 22.20 或更新版本；命令格式见 [skills 官方说明](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)。

默认安装到当前项目，运行后选择要使用的 Agent。想全局安装到 Codex，并跳过交互选择，可以这样写：

```sh
npx skills add LIghtJUNction/draw-project-meme -g -a codex -y
```

想先查看仓库里有哪些技能：

```sh
npx skills add LIghtJUNction/used-car-video-copywriting-skill --list
```

安装器会处理技能目录和配套文件；技能依赖的外部程序、模型和游戏环境仍按原仓库说明准备。本仓库只做索引，安装命令指向各自的源仓库。

## 完整目录

<!-- stats:start -->
截至 2026-11-03（UTC），检查了 **100** 个公开非 Fork 仓库，其中 **42** 个仓库有技能，共 **152** 个 `SKILL.md` 文件入口。这是文件入口数量，未按名称或内容去重。汇总仓库本身不计入扫描。
<!-- stats:end -->

完整路径见 **[CATALOG.md](CATALOG.md)**，机器可读数据见 [data/catalog.json](data/catalog.json)。同名技能可能在多个项目里出现，目录保留来源，不把它们算成不同的原创技能。

收录范围是 `LIghtJUNction` 账号下公开、非 Fork 仓库默认分支中的 `SKILL.md`。不包含私有仓库、组织仓库、其他分支、子模块内部文件，以及只有运行命令才会生成的技能。项目里随附的第三方技能也会出现在完整目录中；仓库属于我，不代表里面每个技能都是我原创。

归档仓库单独标注。这里只核对公开文件是否存在，不代表每个技能都经过当前环境的运行验证。原技能的许可和署名以来源仓库为准。

## 更新目录

需要 Python 3、GitHub CLI 和可用的 GitHub 访问权限，无额外 Python 依赖。

```sh
python3 scripts/catalog.py refresh
python3 scripts/catalog.py check
```

`refresh` 读取 GitHub 的仓库列表和文件树，更新数据、首页统计和完整目录。遇到请求失败或文件树截断会停止，保留上一次结果。它不下载或执行技能，也不读取技能正文。

首页简介在 [data/highlights.json](data/highlights.json) 中维护。只改文案时运行：

```sh
python3 scripts/catalog.py render
python3 scripts/catalog.py check
```

## 自动检查和更新

[![Catalog](https://github.com/LIghtJUNction/skills/actions/workflows/catalog.yml/badge.svg)](https://github.com/LIghtJUNction/skills/actions/workflows/catalog.yml)

- 推送到 `main` 或提交 PR 时，CI 检查目录结构、安装命令生成和文档一致性。
- 每天台北时间 **10:23**（UTC 02:23）计划扫描公开仓库，检查通过后自动提交目录变化。GitHub 的定时任务可能延迟。
- 也可以在 [Actions → Catalog](https://github.com/LIghtJUNction/skills/actions/workflows/catalog.yml) 点击 **Run workflow** 手动更新。
- 没有变化就不产生提交；扫描失败或结果不完整时保留原目录，并在 Actions 中报错。

自动任务只维护目录，不安装或执行源仓库中的技能。安装命令按官方支持的源地址生成，不等同于每个源技能均已通过安装实测。

本地可以运行与 CI 相同的检查：

```sh
python3 -m unittest discover -s tests -v
python3 scripts/catalog.py check
```
