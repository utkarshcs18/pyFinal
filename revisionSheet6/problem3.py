l = ["Ayush", "Akash", "Brook", "Ashoka"]

name = input("Enter your name: ")

if(name.capitalize() in l):
    print(f'{name} is in List')
else:
    print(f'{name} not in List')
