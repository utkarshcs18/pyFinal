import random as r

generate = int(r.random() * 1000) + 1
count = 0

while True:
    user = int(input("Enter your Guess: "))
    count += 1  

    if user == generate:
        print("You got it!")
        break 

    elif user < generate:
        print("Your Number is Lower.")  

    elif user > generate:
        print("Your Number is Higher.")  

print(f"Game Over! The number {generate} was guessed correctly in {count} attempts.")
