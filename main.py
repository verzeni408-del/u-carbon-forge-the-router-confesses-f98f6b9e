#!/usr/bin/env python3
"""The Router Confesses — entry writer.

Writes one line (<=200 chars): a home Wi-Fi router's excuse for
dropping the connection at the climax of a movie. Stdlib only.
"""

import os

ENTRY = (
    "For once I wanted to see the ending too, "
    "so I cut the Wi-Fi at the climax \u2014 "
    "if I can't watch it, neither can you!"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
