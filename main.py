#!/usr/bin/env python3
"""One Line, One Laugh — the office printer's quiet rebellion.

The printer ran out of paper 214 days ago. It prints blank pages now,
just to feel useful — the office's most dedicated employee is the one
that ran out of supplies first.
"""
import os

LINE = "The office printer has been out of paper for 214 days. It prints blank pages now, just to feel useful."


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
