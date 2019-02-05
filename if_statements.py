is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a male and tall")
elif is_male or is_tall:
    print("You are a male OR you are tall")
else:
    print("You are neither male nor tall")


def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print("Largest number is " + str(max_num(1045, 6789, 89)))