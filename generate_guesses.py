#!/usr/bin/env python3
# generate_guesses.py
# Usage: python3 generate_guesses.py First Last domain.com
# Example: python3 generate_guesses.py "Bob" "Gormer" "example.com"

import sys
from pathlib import Path

if len(sys.argv) != 4:
    print("Usage: python3 generate_guesses.py First Last domain.com")
    sys.exit(1)

first = sys.argv[1].strip().lower()
last = sys.argv[2].strip().lower()
domain = sys.argv[3].strip().lower()

f = first[0] if first else ""
l = last[0] if last else ""
m = ""  # if you want to include middle initial, you can modify script to accept it

# List of templates. Each template uses placeholders: {first}, {last}, {f}, {l}, {m}
templates = [
    "{first}@{domain}",
    "{last}@{domain}",
    "{first}.{last}@{domain}",
    "{first}_{last}@{domain}",
    "{first}-{last}@{domain}",
    "{f}{last}@{domain}",
    "{first}{l}@{domain}",
    "{f}.{last}@{domain}",
    "{first}.{l}@{domain}",
    "{first}{last}@{domain}",
    "{last}{first}@{domain}",
    "{last}.{first}@{domain}",
    "{l}{first}@{domain}",
    "{first}{l}1@{domain}",
    "{first}{l}01@{domain}",
    "{f}{last}1@{domain}",
    "{first}.{last}1@{domain}",
    "{first}{last}123@{domain}",
    "{last}{f}@{domain}",
    "{first}{_}{last}@{domain}".replace("{_}","_"),  # identical to first_last but left as example
    "{first[0:3]}{last}@{domain}".replace("{first[0:3]}", first[:3]),
    "{first[:2]}{last[:2]}@{domain}".replace("{first[:2]}", first[:2]).replace("{last[:2]}", last[:2]),
    "{f}{l}@{domain}",
    "{first}{last[:1]}@{domain}".replace("{last[:1]}", last[:1]),
    "{first}-{l}@{domain}".replace("{l}", l),
    "{first}.{last[0:2]}@{domain}".replace("{last[0:2]}", last[:2]),
    "{first}{last}0@{domain}",
    "{first}.{last[0]}@{domain}".replace("{last[0]}", last[:1]),
    "{first[0]}{last}@{domain}".replace("{first[0]}", f),
    "{first}{last}01@{domain}",
    "{first}.{last}.work@{domain}",
    "{first}.{last}.office@{domain}",
    "{first}{last}.eng@{domain}",
    "{first}{last}.me@{domain}",
    "{first}.{last}{2}@{domain}".replace("{2}", "2"),
    "{f}{last}99@{domain}",
    "{first}{last}1980@{domain}",
    "{first}{last}1990@{domain}",
    "{first}{last}20@{domain}",
    "{first}.{last}.{m}@{domain}".replace("{m}", m),
    "{last}.{first}@{domain}",
    "{last}{first[:1]}@{domain}".replace("{first[:1]}", first[:1]),
    "{first}{last[0:3]}@{domain}".replace("{last[0:3]}", last[:3]),
    "{f}-{last}@{domain}".replace("{f}", f),
    "{first}_{l}@{domain}".replace("{l}", l),
    "{first}{l}99@{domain}".replace("{l}", l),
    "{f}{last}01@{domain}".replace("{f}", f),
    "{first}.{last}{l}@{domain}".replace("{l}", l),
    "{first}{last}{f}@{domain}".replace("{f}", f),
    "{last}.{f}@{domain}".replace("{f}", f),
    "{first[0:2]}.{last}@{domain}".replace("{first[0:2]}", first[:2]),
    "{first}{last}.team@{domain}",
    "{first}.{last}.team@{domain}",
    "{first}{last}.{l}@{domain}".replace("{l}", l),
    "{first}.{l}{last}@{domain}".replace("{l}", l),
    "{first}.{last[0:3]}@{domain}".replace("{last[0:3]}", last[:3]),
    "{f}{l}{last}@{domain}".replace("{f}", f).replace("{l}", l),
    "{first}-{last[:2]}@{domain}".replace("{last[:2]}", last[:2]),
    "{first}{last}_eng@{domain}",
    "{first}.{last}_eng@{domain}",
    "{first}{last}eng@{domain}",
    "{first}.{l}{last}@{domain}".replace("{l}", l),
    "{first}{last}01@{domain}",
    "{first}.{last}01@{domain}",
    "{first}{last}02@{domain}",
    "{first}{last}03@{domain}",
    "{first}.{last}.01@{domain}",
    "{f}{last}_01@{domain}".replace("{f}", f),
    "{first}{last}_01@{domain}",
    "{last}_{first}@{domain}",
    "{last}.{first}01@{domain}",
    "{first}{last}jr@{domain}",
    "{first}{last}sr@{domain}",
    "{first}.{last}jr@{domain}",
    "{first}.{last}sr@{domain}",
    "{first}{last}.mail@{domain}",
    "{first}.{last}.mail@{domain}",
    "{first}{last}@{domain}".replace("{first}", first).replace("{last}", last),  # replication for safety
]

# The list above may have less than 100 due to dynamic building; we'll build more by adding numbered suffixes
guesses = []
for t in templates:
    # format each template safely
    try:
        addr = t.format(first=first, last=last, f=f, l=l, m=m, domain=domain)
    except Exception:
        addr = t.replace("{first}", first).replace("{last}", last).replace("{f}", f).replace("{l}", l).replace("{m}", m).replace("{domain}", domain)
    guesses.append(addr)

# add numbered variants until we have 100 unique guesses
i = 1
while len(guesses) < 100:
    candidate = f"{first}.{last}{i}@{domain}"
    if candidate not in guesses:
        guesses.append(candidate)
    i += 1

# ensure unique order
guesses = list(dict.fromkeys(guesses))[:100]

out = Path.home() / "Documents" / f"{first}_{last}_email_guesses.csv"
out.parent.mkdir(parents=True, exist_ok=True)
with out.open("w", encoding="utf-8") as fh:
    fh.write("email\n")
    for g in guesses:
        fh.write(g + "\n")

print(f"Wrote {len(guesses)} guesses to {out}")
