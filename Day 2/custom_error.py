class NegativeNumberError(ValueError):
    pass

def get_positive_number():
    while True:
        try:
            num_str = input("Please enter a positive number: ")
            number = float(num_str)

            if number < 0:
                raise NegativeNumberError("Number must be positive.")
            return number

        except NegativeNumberError as e:
            print(f"NegativeNumberError: {e}")
        except ValueError:
            print("ValueError: Please enter a valid number.")

if __name__ == "__main__":
    try:
        positive_num = get_positive_number()
        print(f"You entered: {positive_num}")
    except NegativeNumberError:
        print("Caught a NegativeNumberError in main.")
    except Exception as e:
        print("Unexpected error:", e)

