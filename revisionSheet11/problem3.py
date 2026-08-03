try:
    with open('revisionSheet11/1.txt', 'r') as a, open('revisionSheet11/2.txt', 'r') as b, open('revisionSheet11/3.txt', 'r') as c:
        print(a.read(),b.read(),c.read())

except FileNotFoundError as e:
    print(f"File not found {e}")

else:
    print("Found and Printed....")



