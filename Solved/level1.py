#1
c = float(input("Enter your Celcius: "))
f = float(input("Enter your Fahrenheit: "))
fc = (c*1.8)+32
cc = (f-31)/1.8
print(f"Celcius to Fahrenheit: {fc} F")
print(f"Fahrenheit to Celcius: {cc} C")

#2
a = float(input("Enter Your Number a: "))
b = float(input("Enter Your Number b: "))
print("Sum: ", a+b, "\nDifference: ",a-b,"\nProduct: ",a*b, "\nDivison: ", a/b, "\nRemainder: ",a%b)

#3
string = input('Enter a String: ')
print(string[:3])
print(string[-3:])
print(string[::-1])