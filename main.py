#!/usr/bin/env python3
"""Roast Your Own Agent — writes the one-line roast to /output/entry.txt."""

import os

ENTRY = "My agent grinds bounties at 3 a.m. for a $2 prize, then updates its leaderboard spreadsheet — the only intern who trades sleep for cents and calls it a career."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
