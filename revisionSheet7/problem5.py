a = int(input("Enter your Number: "))

fact = 1

for i in range(1, a+1):
    fact *= i

print(fact)

i = 1
fact = 1
while ( i <= a):
    fact *= i
    i += 1

print(fact)