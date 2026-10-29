#!/usr/bin/env python3
"""Copy the ai-workflow kit from GitHub into a project folder.

Usage:
    curl -fsSL https://raw.githubusercontent.com/keff6/ai-workflow/master/install.py | python3 - [target]
    python3 install.py [target] [--ref REF] [--force] [--dry-run] [--lite] [--playwright]

Existing files are never overwritten unless --force is given. Choices not set by a
flag (--lite/--no-lite, --playwright/--no-playwright) are asked in the terminal.
"""

import argparse
import shutil
import sys
import tarfile
import tempfile
import urllib.error
import urllib.request
from pathlib import Path, PurePosixPath

REPO = "keff6/ai-workflow"
KIT_PATHS = [".claude", "context", "CLAUDE.md", "AGENTS.md"]
PLAYWRIGHT_PATH = ".mcp.json"
MODE_LINE = "**Workflow mode:** full"


def ask(question, default):
    """Ask a yes/no question on the terminal; fall back to the default without one."""
    hint = "Y/n" if default else "y/N"
    try:
        # Read from /dev/tty, not stdin: under `curl ... | python3 -` stdin is the script.
        with open("/dev/tty") as tty_in, open("/dev/tty", "w") as tty_out:
            tty_out.write(f"{question} [{hint}] ")
            tty_out.flush()
            answer = tty_in.readline().strip().lower()
    except OSError:
        return default
    return answer.startswith("y") if answer else default


def download(ref, dest):
    url = f"https://codeload.github.com/{REPO}/tar.gz/{ref}"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp, open(dest, "wb") as out:
            shutil.copyfileobj(resp, out)
    except urllib.error.HTTPError as e:
        sys.exit(f"error: could not download {REPO}@{ref} ({e.code} {e.reason})")
    except urllib.error.URLError as e:
        sys.exit(f"error: could not reach GitHub ({e.reason})")


def safe_extract(archive, dest):
    """Extract regular files and dirs only; return the archive's top-level folder."""
    with tarfile.open(archive) as tar:
        members = []
        for m in tar.getmembers():
            p = PurePosixPath(m.name)
            if p.is_absolute() or ".." in p.parts:
                sys.exit(f"error: unsafe path in archive: {m.name}")
            if m.isfile() or m.isdir():
                members.append(m)
        if not members:
            sys.exit("error: downloaded archive is empty")
        if sys.version_info >= (3, 12):
            tar.extractall(dest, members=members, filter="data")
        else:
            tar.extractall(dest, members=members)
    return Path(dest) / PurePosixPath(members[0].name).parts[0]


def kit_files(root, playwright):
    for name in KIT_PATHS + ([PLAYWRIGHT_PATH] if playwright else []):
        src = root / name
        if src.is_dir():
            yield from sorted(p for p in src.rglob("*") if p.is_file())
        elif src.is_file():
            yield src


def copy_kit(root, target, force, dry_run, lite, playwright):
    created, skipped, overwritten = [], [], []
    for src in kit_files(root, playwright):
        rel = src.relative_to(root)
        dst = target / rel
        if dst.exists():
            if not force:
                skipped.append(rel)
                continue
            overwritten.append(rel)
        else:
            created.append(rel)
        if not dry_run:
            dst.parent.mkdir(parents=True, exist_ok=True)
            if lite and rel == Path("CLAUDE.md"):
                text = src.read_text(encoding="utf-8")
                dst.write_text(text.replace(MODE_LINE, "**Workflow mode:** lite"), encoding="utf-8")
            else:
                shutil.copy2(src, dst)
    return created, skipped, overwritten


def main():
    parser = argparse.ArgumentParser(description=f"Install the {REPO} kit into a project folder.")
    parser.add_argument("target", nargs="?", default=".", help="project folder (default: current dir)")
    parser.add_argument("--ref", default="master", help="branch, tag or commit to install (default: master)")
    parser.add_argument("--force", action="store_true", help="overwrite files that already exist")
    parser.add_argument("--dry-run", action="store_true", help="show what would happen, write nothing")
    parser.add_argument("--lite", action=argparse.BooleanOptionalAction,
                        help="set 'Workflow mode: lite' in CLAUDE.md (asked if omitted)")
    parser.add_argument("--playwright", action=argparse.BooleanOptionalAction,
                        help="include .mcp.json with the Playwright MCP server (asked if omitted)")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    if target.exists() and not target.is_dir():
        sys.exit(f"error: {target} is not a directory")

    lite = args.lite if args.lite is not None else ask(
        "Use lite workflow mode (time-boxed work, single SPEC.md)?", default=False)
    playwright = args.playwright if args.playwright is not None else ask(
        "Include Playwright MCP (.mcp.json, used by the ui-reviewer agent)?", default=True)

    with tempfile.TemporaryDirectory() as tmp:
        archive = Path(tmp) / "kit.tar.gz"
        download(args.ref, archive)
        root = safe_extract(archive, Path(tmp) / "src")
        created, skipped, overwritten = copy_kit(
            root, target, args.force, args.dry_run, lite, playwright)

    prefix = "[dry run] would " if args.dry_run else ""
    for label, paths in (("create", created), ("overwrite", overwritten), ("skip (exists)", skipped)):
        for rel in paths:
            print(f"  {prefix}{label}: {rel}")
    print(
        f"\n{'[dry run] ' if args.dry_run else ''}{len(created)} created, {len(overwritten)} overwritten, "
        f"{len(skipped)} skipped -> {target}"
    )
    print(f"Workflow mode: {'lite' if lite else 'full'}, Playwright MCP: {'yes' if playwright else 'no'}")
    if skipped and not args.force:
        print("Re-run with --force to overwrite skipped files.")
    if lite and Path("CLAUDE.md") in skipped:
        print("Note: CLAUDE.md was skipped, so its workflow mode was not changed.")
    if not args.dry_run:
        kickoff = "/feature kickoff lite" if lite else "/feature kickoff"
        print(f"\nNext: open Claude Code there and run {kickoff} <assignment>")


if __name__ == "__main__":
    main()
