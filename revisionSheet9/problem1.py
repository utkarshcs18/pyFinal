def read():
    
    with open("revisionSheet9/poem.txt") as f:
        poem = f.read()

    print(poem)

    if "abc" in poem:
        print(f"\n\n abc is in the poem....")

read()



