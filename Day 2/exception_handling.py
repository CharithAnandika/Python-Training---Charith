try :
    a=1
    for a in range(1,3):
        numer_input = input("Enter Numerator: ")
        numer = float(numer_input)

        den_input = input("Enter Denominator : ")
        den = float(den_input)

        result = numer/den

        print(result)

except ValueError:
    print("Value error")
except ZeroDivisionError:
    print("ZeroDivisionError")
except Exception as e :
    print("unexpected error")
