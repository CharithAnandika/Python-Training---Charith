try :

    for number in range (1,4):
        number = int(input("Enter mark : "))
    
        while 100 < number or number < 0 :
            print("Invalid number")
            number = int(input("Enter mark : "))

        if number >= 75 :
            print("Your grade is A")
        elif number >= 65 :
            print("Your grade is B")
        elif number >= 50 :
            print("Your grade is C")
        elif number >= 35 :
            print("Your grade is S")   
        else:
            print("Your grade is F") 

    
except :
    print("Invalid number-1")
    