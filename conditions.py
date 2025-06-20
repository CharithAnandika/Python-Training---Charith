try:

    number = int(input("Enter Number : "))

    if number > 0 :
        print(f"The number {number} is positive")
    elif number < 0 :
        print(f"The number {number} is negative")
    else:
        print(f"The number {number} is zero") 

except ValueError :
    print("Invalid Number")

