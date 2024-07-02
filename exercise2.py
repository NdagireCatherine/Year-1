#number 2
"""import random
secret_num = random.randint(1, 20)
print("Hey Welcome!")
guesses = 0
guess=int(input("guess:"))
if guess == secret_num:
    print("Well guessed!")
else:
    print("Try again!")"""

#number 4
"""user_word =input("Enter the word:")
reversed_word = user_word[::-1]
print(f"The reversed word is: {reversed_word}")"""


#number 8
"""def mult():
    num=int(input("Input a number:"))
    for i in range (10):
        multiple = num * i
        print(multiple)
mult()"""


#number 12
"""word = input("Enter a word:")
uppercase = 0
lowercase = 0

for char in word:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
print(f"Uppercase:{uppercase}")
print(f"Lowercase:{lowercase}")"""

#number 13
"""import re
def check_password():
    password = input("Enter your password:")
    feedback =[]
    if len(password) < 8:
        feedback.append("Password should exceed 8 characters.")
    if not len(password) > 16:
        feedback.append("Password should not exceed 16 characters.")
    if not re.search("[A-Z]", password):
        feedback.append("Password must contain at least one uppercase letter.")
    if not re.search("[a-z]", password):
        feedback.append("Password must contain atleast one lowercase letter.")
    if not re.search("[0-9]", password):
        feedback.append("Password must contain at least one digit.")
    if not re.search("[$%&]", password):
        feedback.append("Password must contain 1 character from $%&.")
    if len(feedback) > 0:
        return False, feedback
    else:
        return True, []
valid = check_password()  
if valid:
    print("Password is valid.")  
else:
    print("Password is invalid.")"""


#number 39
"""def check_number():
    num = float(input("Enter a number:"))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
check_number()"""

#number 50
"""def print_pattern():
    num = 0
    for i in range (0,9):
        for j in range(i):
            print(num, end=" ")
        print()
print_pattern()"""

#number 41
"""def sum(num1, num2, num3):
    add = num1 + num2 +num3
    if 25 <= add <= 35:
        print("35")
    else:
        print(add)
sum(25, 10, 0)"""

#number 9
"""for i in range (1,81):
    if i % 3 == 0 and i % 7 == 0:
        print("fizzbuzz")
    elif i % 3 ==0:
        print("fizz")
    elif i % 7 ==0:
        print("buzz")
    else:
        print(i)"""

#number 1
for i in range (2000, 3201):
    if i % 8 == 0 and i % 6 ==0:
        print(i)

