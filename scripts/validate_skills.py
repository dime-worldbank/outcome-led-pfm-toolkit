#!/usr/bin/env python3
"""Validate every skill under skills/.

Checks, for each skills/<name>/ folder:
  - SKILL.md exists
  - it starts with YAML frontmatter containing non-empty `name` and `description`
  - `name` matches the folder name and is lowercase with hyphens only
  - SKILL.md is under 500 lines (warning only)
  - no unexpected top-level files or folders inside the skill

No third-party dependencies. Exit code 1 on any error.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ALLOWED_DIRS = {"scripts", "references", "assets", "evals"}
ALLOWED_FILES = {"SKILL.md", "README.md", "LICENSE", "LICENSE.md", "LICENSE.txt"}
MAX_LINES = 500


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Return the frontmatter as a flat dict, or None if missing/malformed.

    Only simple `key: value` lines are supported, which is all SKILL.md needs.
    """
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            return None
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def validate_skill(skill_dir: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    rel = skill_dir.relative_to(ROOT)

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"{rel}: missing SKILL.md")
        return errors, warnings

    text = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        errors.append(f"{rel}/SKILL.md: missing or malformed YAML frontmatter")
    else:
        name = fm.get("name", "")
        desc = fm.get("description", "")
        if not name:
            errors.append(f"{rel}/SKILL.md: frontmatter has no `name`")
        elif not NAME_RE.match(name):
            errors.append(f"{rel}/SKILL.md: name '{name}' must be lowercase letters, digits and hyphens")
        elif name != skill_dir.name:
            errors.append(f"{rel}/SKILL.md: name '{name}' does not match folder '{skill_dir.name}'")
        if not desc:
            errors.append(f"{rel}/SKILL.md: frontmatter has no `description`")
        elif len(desc) < 40:
            warnings.append(f"{rel}/SKILL.md: description is very short; say what it does and when to use it")

    line_count = text.count("\n") + 1
    if line_count > MAX_LINES:
        warnings.append(f"{rel}/SKILL.md: {line_count} lines, consider moving material to references/")

    for child in skill_dir.iterdir():
        if child.name.startswith("."):
            continue
        if child.is_dir() and child.name not in ALLOWED_DIRS:
            warnings.append(f"{rel}/{child.name}/: unexpected folder (expected one of {sorted(ALLOWED_DIRS)})")
        elif child.is_file() and child.name not in ALLOWED_FILES:
            warnings.append(f"{rel}/{child.name}: unexpected top-level file")

    return errors, warnings


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"error: {SKILLS_DIR} does not exist")
        return 1

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and not p.name.startswith((".", "_")))
    if not skill_dirs:
        print("no skills found under skills/")
        return 0

    all_errors: list[str] = []
    all_warnings: list[str] = []
    for skill_dir in skill_dirs:
        errors, warnings = validate_skill(skill_dir)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        status = "FAIL" if errors else "ok"
        print(f"[{status}] {skill_dir.name}")

    for w in all_warnings:
        print(f"warning: {w}")
    for e in all_errors:
        print(f"error: {e}")

    print(f"\n{len(skill_dirs)} skill(s), {len(all_errors)} error(s), {len(all_warnings)} warning(s)")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
