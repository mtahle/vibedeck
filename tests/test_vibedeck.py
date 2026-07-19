import importlib.util
from datetime import date
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


bootstrap_module = load_module(
    "bootstrap_project_os",
    ROOT / "skills" / "project-os" / "scripts" / "bootstrap_project_os.py",
)
install_module = load_module("install", ROOT / "scripts" / "install.py")


class BootstrapTests(unittest.TestCase):
    def test_creates_canonical_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            created = bootstrap_module.bootstrap(root, date(2026, 7, 19))
            self.assertEqual(created, ["PROJECT_CONTROL.md", "STATUS.md"])
            control = (root / "PROJECT_CONTROL.md").read_text(encoding="utf-8")
            status = (root / "STATUS.md").read_text(encoding="utf-8")
            self.assertIn("Last reconciled: 2026-07-19", control)
            self.assertIn("Initialized VibeDeck", status)

    def test_never_overwrites_existing_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            control = root / "PROJECT_CONTROL.md"
            control.write_text("owner data\n", encoding="utf-8")
            created = bootstrap_module.bootstrap(root, date(2026, 7, 19))
            self.assertEqual(created, ["STATUS.md"])
            self.assertEqual(control.read_text(encoding="utf-8"), "owner data\n")


class InstallTests(unittest.TestCase):
    def test_installs_skill_and_requires_force_for_replacement(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "skills" / "project-os"
            installed = install_module.install(
                ROOT / "skills" / "project-os",
                destination,
            )
            self.assertTrue((installed / "SKILL.md").is_file())
            with self.assertRaises(FileExistsError):
                install_module.install(
                    ROOT / "skills" / "project-os",
                    destination,
                )

    def test_force_replaces_existing_skill(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "skills" / "project-os"
            destination.mkdir(parents=True)
            (destination / "stale.txt").write_text("stale", encoding="utf-8")
            install_module.install(
                ROOT / "skills" / "project-os",
                destination,
                force=True,
            )
            self.assertFalse((destination / "stale.txt").exists())
            self.assertTrue((destination / "SKILL.md").is_file())


class PackageTests(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            "README.md",
            "LICENSE",
            "templates/AGENTS.snippet.md",
            "skills/project-os/SKILL.md",
            "skills/project-os/references/commands.md",
            "skills/project-os/agents/openai.yaml",
        ]
        for relative_path in required:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((ROOT / relative_path).is_file())

    def test_skill_frontmatter_and_commands(self):
        skill = (ROOT / "skills/project-os/SKILL.md").read_text(encoding="utf-8")
        commands = (ROOT / "skills/project-os/references/commands.md").read_text(
            encoding="utf-8"
        )
        self.assertTrue(skill.startswith("---\nname: project-os\n"))
        for command in (
            "/log",
            "/next",
            "/urgent",
            "/decision",
            "/os-status",
            "/dashboard",
            "/resume",
            "/help",
        ):
            self.assertIn(command, commands)


if __name__ == "__main__":
    unittest.main()
