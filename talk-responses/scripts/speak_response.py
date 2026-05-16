#!/usr/bin/env python3
"""Speak Codex response text aloud with macOS `say`."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys


MAX_CHARS_DEFAULT = 4000
MAX_INPUT_CHARS_DEFAULT = 100_000


def sanitize(text: str, max_chars: int, max_input_chars: int) -> str:
    if len(text) > max_input_chars:
        text = text[:max_input_chars]
    text = text.strip()
    text = re.sub(r"```.*?```", " code block omitted. ", text, flags=re.DOTALL)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"https?://\S+", " link omitted ", text)
    text = re.sub(r"\s+", " ", text)
    if len(text) > max_chars:
        text = text[:max_chars].rstrip() + " ... response truncated for speech."
    return text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Speak response text with macOS say.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--stdin", action="store_true", help="Read text from stdin.")
    source.add_argument("--text", default="", help="Text to speak.")
    parser.add_argument("--voice", default="", help="Optional macOS say voice.")
    parser.add_argument("--rate", type=int, default=0, help="Optional speech rate.")
    parser.add_argument("--max-chars", type=int, default=MAX_CHARS_DEFAULT)
    parser.add_argument("--max-input-chars", type=int, default=MAX_INPUT_CHARS_DEFAULT)
    parser.add_argument("--dry-run", action="store_true", help="Print sanitized text without speaking.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    raw_text = sys.stdin.read() if args.stdin else args.text
    text = sanitize(raw_text, max(1, args.max_chars), max(1, args.max_input_chars))
    if not text:
        return 0

    if args.dry_run:
        print(text)
        return 0

    say_path = "/usr/bin/say" if Path("/usr/bin/say").exists() else shutil.which("say")
    if not say_path:
        print("macOS `say` command not found.", file=sys.stderr)
        return 127

    cmd = [say_path]
    if args.voice:
        cmd.extend(["-v", args.voice])
    if args.rate > 0:
        cmd.extend(["-r", str(args.rate)])
    cmd.append(text)
    subprocess.run(cmd, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
