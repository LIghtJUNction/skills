import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    "catalog", Path(__file__).resolve().parents[1] / "scripts/catalog.py")
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(catalog.DATA.read_text())

    def test_commands_target_skill_directory(self):
        repo = {"repo": "LIghtJUNction/example", "branch": "main"}
        self.assertEqual(catalog.install_command(repo, "SKILL.md"),
                         "npx skills add LIghtJUNction/example")
        self.assertEqual(catalog.install_command(repo, "docs/skills/demo/SKILL.md"),
                         "npx skills add https://github.com/LIghtJUNction/example/tree/main/docs/skills/demo")

    def test_invalid_catalog_rejected(self):
        for field, value in [("truncated", True), ("paths", ["../SKILL.md"])]:
            with self.subTest(field=field):
                bad = copy.deepcopy(self.data)
                bad["repositories"][0][field] = value
                with self.assertRaises(AssertionError):
                    catalog.validate(bad)

    def test_failed_refresh_preserves_previous_files(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "catalog.json"
            target.write_text(json.dumps(self.data))
            before = target.read_bytes()
            with patch.object(catalog, "DATA", target), \
                 patch.object(catalog, "discover", side_effect=RuntimeError("API failure")), \
                 patch("sys.argv", ["catalog.py", "refresh"]):
                with self.assertRaises(RuntimeError):
                    catalog.main()
            self.assertEqual(target.read_bytes(), before)

    def test_unchanged_refresh_does_not_change_timestamp(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "catalog.json"
            target.write_text(json.dumps(self.data, ensure_ascii=False, indent=2) + "\n")
            before = target.read_bytes()
            fresh = copy.deepcopy(self.data)
            fresh["checked_at"] = "2099-01-01T00:00:00+00:00"
            with patch.object(catalog, "DATA", target), \
                 patch.object(catalog, "discover", return_value=fresh), \
                 patch.object(catalog, "outputs", return_value={}), \
                 patch("sys.argv", ["catalog.py", "refresh"]), \
                 contextlib.redirect_stdout(io.StringIO()):
                catalog.main()
            self.assertEqual(target.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
