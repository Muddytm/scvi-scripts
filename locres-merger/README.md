# locres file merger

Quick way to merge locres text files.

1. Put your current locres in this directory as Games.locres.txt. This file will be modified by the script.

2. Put the locres from the mod you'd like to add in this directory as well, and rename it to Mod.locres.txt.

3. Double click merge.bat file, or run merge.py with Python.

4. Game.locres.txt will update with any changes you've made, and existing changes will not be overwritten. :)

If an already-modified line of text in Game.locres.txt would be overwritten by a new line in Mod.locres.txt, nothing will be changed and errors.log will be updated to reflect what lines conflict.
