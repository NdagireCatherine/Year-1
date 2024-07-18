#1. Write a python function to find the maximum of three numbers.
def max():
    num1=int(input("Enter the 1st number:"))
    num2=int(input("Enter the 2nd number:"))
    num3=int(input("Enter the 3rd number:"))
    if num1 >= num2 and num1 >=num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max())


#2. Write a python function to sum all the numbers in a list.
list_of_numbers = input("Enter a list of numbers:")
list_of_numbers = [int(x) for x in list_of_numbers.split()]
sum = 0
for num in list_of_numbers:
    sum += num
print("Sum of numbers=", sum)


#3. Write a python function to multiply all the numbers in a list.
import math
def multiply(numbers):
    return math.prod(numbers)
numbers = [1, 2, 3, 4, 5]
print(multiply(numbers))


#5. Write a python function to calculate the factorial of a number. The function accepts the number as an argument.
import  math
def factorial(num):
    return math.factorial(num)
num = 7
print(factorial(num))


#9. Write a pyhton function that takes a number as a parameter and checks whether the number is a prime or not.
def prime():
    x = int(input("Enter a number:"))
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) +1):
        if x % i == 0:
            return False
    return True
if prime():
    print("Is prime number.")
else:
    print("Is not a prime number.")





