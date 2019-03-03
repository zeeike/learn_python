try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as:
    print("Invalid input")

#Best practice is to except for specific errors
