try:
    a = int(input("Enter your numerator: "))
    b = int(input("Enter your denominator: "))

    if(b == 0):
        raise ZeroDivisionError("Check your denominator....")
    else:
        print(f"Result: {a/b}")

# except ZeroDivisionError as e:
#     print(f"Error {e}")

except ValueError as e:
    print(f"Error {e}")

else:
    print("Completed")
 
