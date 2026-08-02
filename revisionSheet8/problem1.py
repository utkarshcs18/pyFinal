def greatest(a,b,c):
    if a > b and a  > c:
        print("a is greatest")
    elif b > a and b > c:
        print("b is greatest")
    else:
        print("c is greatest")

a = int(input("Enter your 1st Number: "))
b = int(input("Enter your 1st Number: "))
c = int(input("Enter your 1st Number: "))

greatest(a,b,c)