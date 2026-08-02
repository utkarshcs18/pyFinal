def c2f(c):
    f = (c*9/5) +  32

    return f


c = int(input("Enter your degree in celcius: "))

print(f'Celcius to Fahrenheit: {c2f(c)}')