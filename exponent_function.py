def raise_to_power(base_num,power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    print (result)

base = int(input("Please enter the base number:"))

power = int(input("Please enter the number to power:"))

raise_to_power(base,power)