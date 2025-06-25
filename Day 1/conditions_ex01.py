try:

    mark = int(input("Enter mark : "))

    if mark >= 75 :
        print("Your grade is A")
    elif mark >= 65 :
        print("Your grade is B")
    elif mark >= 50 :
        print("Your grade is C")
    elif mark >= 35 :
        print("Your grade is S")   
    else:
        print("Your grade is F")   

except :
    print("Invalid Mark")