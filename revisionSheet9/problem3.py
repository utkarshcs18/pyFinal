word = "Donkey"

with open("revisionSheet9/words.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("revisionSheet9/words.txt", "w") as f:
    f.write(contentNew)