a = int(input("Enter your Number 1: "))
b = int(input("Enter your Number 2: "))
c = int(input("Enter your Number 3: "))
d = int(input("Enter your Number 4: "))

if a > b and a > c and a > d:
    print(f"{a} is greatest")
elif b > a and b > c and b > d:
    print(f"{b} is greatest")
elif c > a and c > b and c > d:
    print(f"{c} is greatest")
else:
    print(f"{d} is greatest")