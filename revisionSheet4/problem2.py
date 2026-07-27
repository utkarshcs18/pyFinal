marks = []

for i in range(6):
    inputMarks = int(input("Enter Students marks: "))
    marks.append(inputMarks)


# change the whole list
marks.sort()
print(marks)

# OR

new = sorted(marks)
print(new)