try:
    user_input = input("Eneter a list of numbers seperated by commas : ")
    numbers_str = user_input.split(',')
    numbers = []

    if not numbers_str or (len(numbers_str) == 1 and not numbers_str[0]):
        raise IndexError("The list is empty.")
    
    for x in numbers_str:
        numbers.append(int(x.strip()))

except ValueError:
    print("ValeError")
except IndexError as e:
    print("IndexError")
else :
    total_sum = sum(numbers)
    print(total_sum)