from pathlib import Path

path = Path("words.txt")

txtFile = path.read_text()

print(txtFile)