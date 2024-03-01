# Open a file and print the text.

from pathlib import Path

path = Path("words.txt")

txtFile = path.read_text()

print(txtFile)