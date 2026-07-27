#1
year = int(input("Enter your Year: "))

if(year <= 0):
    print("Enter Valid Year")

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")


#2
num = int(input("Enter your Number: "))
isPrime = True
count = 0

if(num == 0 or num == 1):
    print("Not a Prime Number.")
else:
    for i in range(2, (num//2) + 1):
        if(num % i == 0):
            isPrime = False
            break

if(isPrime):
    print(f"{num} is Prime")
else:
    print(f"{num} is Not Prime")


#3
for i in range(1, 50+1):
    if (i % 3 == 0 and i % 5 == 0):
        print(f"{i} FIZZBUZZ")
    elif(i % 3 == 0):
        print(f"{i} FIZZ")
    elif(i % 5 == 0):
        print(f"{i} BUZZ")
    else:
        print(i)



#4
end = int(input("Enter your 'End' Number: "))
a = 0
b = 1

while(a <= end):
    print(a)
    nextNum = a + b
    a = b
    b = nextNum