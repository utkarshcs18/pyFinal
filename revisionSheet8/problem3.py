def natural(n):
    if n == 1:
        return 1
    
    return n + natural(n-1)

a = int(input("Enter your 'nth' Term: "))
print(natural(a))
