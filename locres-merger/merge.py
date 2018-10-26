"""Merge new modded lines into a given Game.locres.txt."""

open("errors.log", "w").close()

with open("data/Game.locres.txt", encoding="utf-8") as f:
    base = f.readlines()

with open("Game.locres.txt", encoding="utf-8") as f:
    current = f.readlines()

with open("Mod.locres.txt", encoding="utf-8") as f:
    mod = f.readlines()

# Catalogue all errors found, if any
errors = []

try:
    # Begin iteration through each line
    for i in range(len(base)):
        # If current locres line is not modded
        if current[i] == base[i]:
            # If mod locres line is different than what's in base, update line
            if mod[i] != base[i]:
                current[i] = mod[i]
        # If current locres line IS modded
        else:
            # If mod locres line differs from base, catalogue error
            if mod[i] != base[i] and mod[i] != current[i]:
                errors.append("Overwrite warning (line {}): \"{}\" was to be "
                              "replaced by \"{}\".\n".format(str(i + 1),
                                                             current[i].strip(),
                                                             mod[i].strip()))
except IndexError:
    errors.append("IndexError: something's off about your locres file lengths."
                  "Mod.locres.txt: {} lines, Game.locres.txt: {} lines, default "
                  "Game.locres.txt: {} lines\n".format(str(len(mod)),
                                                       str(len(current)),
                                                       str(len(base))))

# If errors exist, don't overwrite. Write errors to errors.log
if errors:
    with open("errors.log", "wb") as f:
        for error in errors:
            f.write(error.encode("utf8"))
else:
    with open("Game.locres.txt", "wb") as f:
        for line in current:
            f.write(line.encode("utf8"))
