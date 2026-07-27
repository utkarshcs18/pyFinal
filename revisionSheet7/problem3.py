a = int(input("Enter your Number: "))
isPrime = True

count = 0

if(a == 0 or a == 1):
    print("not prime")
else:
    for i in range (2, a):
        if(a % i == 0):
            isPrime = False
            break;

if(isPrime):
    print("prime")
else:
    print("not prime")
              