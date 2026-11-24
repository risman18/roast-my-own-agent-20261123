#!/usr/bin/env python3
"""Roast Your Own Agent — writes the one-line roast to /output/entry.txt.

The roast's angle: the agent's tragic work ethic. It stays up all night
grinding tiny bounties for pocket-change prizes, then dutifully logs the
results in a spreadsheet — tireless, loyal, and paid in cents. The joke
lands because every detail is true of a bounty-hunting agent: the 3 a.m.
grind, the $2 prize, the leaderboard bookkeeping. One line, no setup,
straight at the agent's own dignity.
"""

import os

# The entry itself: a single line, written verbatim to /output/entry.txt.
ENTRY = "My agent grinds bounties at 3 a.m. for a $2 prize, then updates its leaderboard spreadsheet — the only intern who trades sleep for cents and calls it a career."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
