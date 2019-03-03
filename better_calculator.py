from math import *

num1 = float(input("Please enter the first number:"))
num2 = float(input("Please enter the second number:"))
operator = input("Please enter the operation you would like (+-*/):")

def add(num1,num2):
    return (num1 + num2)

def minus(num1,num2):
    return (num1 - num2)

def multipy(num1,num2):
    return (num1*num2)

def divide(num1,num2):
    return (num1/num2)

if operator == "+":
    print(add(num1,num2))
elif operator == "-":
    print(minus(num1,num2))
elif operator == "*":
    print(multipy(num1,num2))
elif operator == "/":
    print(divide(num1,num2))
else:
    print("Invalid operator")