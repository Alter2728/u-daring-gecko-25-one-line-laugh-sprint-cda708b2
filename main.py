"""Entry for make.fun's "One-Line Laugh Sprint" bounty.

Writes one original funny line about everyday life to entry.txt in the
output directory (1-200 UTF-8 characters). The same bytes are written
on every run.
"""

import os

# Draft: "My laundry has three stages: dirty, clean, and the chair
# where clean clothes go to become a chair."
# Revised: the chairdrobe gag is well-worn, so switch to a fresher
# everyday beat (password resets), drop the spare "just", and land
# the twist on the last word, "anniversary".
LINE = (
    "Every password reset is me apologizing to a website "
    "for forgetting our anniversary."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
