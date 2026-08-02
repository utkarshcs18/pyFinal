def rm(lists, word):
    newLists = []
    for i in lists:
        if not (i == word):
            newLists.append(i.strip(word))

    return newLists




lists = ["Ishu","Shubham","Harikat","Python"]
word = input("Enter Word or text want to remove and strip: ")
print(rm(lists, word))


# Enter Word or text want to remove and strip: IshuShubhamHarikatPython
# ['', '', '', '']