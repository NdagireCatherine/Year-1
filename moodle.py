# 2. Character frequency count: Write a python program to count the occurences of each character in a string.
def occurrences():
    s = input("Enter a string:")
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count) 
occurrences()

#4. Concatenate and swap first two characters: Write a python program to concatenate two strings and swap their first two characters.
def concat_and_swap():
    s1 = input("s1=")
    s2 = input("s2=")
    concat_str = s1 + s2
    if len(s1) > 1 and len(s2) > 1:
        swapped_str = s2[0] + s1[0] + s1[1:] + s2[1:]
    else:
        swapped_str = concat_str
    print(swapped_str)
concat_and_swap()

#7. Remove characters at odd indices: Write a python program to remove characters at odd indices from a string
def odd():
    s = input("Enter a string:")
    odd_index = s[::2]
    print(odd_index)
odd()

#10. Reverse a string: Write a python program to reverse a string.
def reverse():
    word = input("Enter a word:")
    reversed_word = word[::-1]
    print(reversed_word)
reverse()

#12. Reversed words in a string: Write a python program to reverse words in a given string.
def reverse():
    s = input('Enter the string:')
    words = s.split()
    reversed_words =  words[::-1]
    join = " ".join(reversed_words)
    print(join)
reverse()

#16. Sum of digits in a string: Write a python program to compute the sum of digits in a string.
def digit_sum():
    s = input("Enter your string:")
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
    print(sum)
digit_sum()

#18. Count character types: Write a python program to count uppercase, lowercase, special characters and numeric values.
def count_characters():
    s = input("Enter a string:")
    uppercase = 0
    lowercase = 0
    character = 0
    numeric = 0
    for i in s:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
        elif i.isdigit():
            numeric += 1
        else:
            character += 1
    print(f"uppercase:{uppercase}")
    print(f"lowercase:{lowercase}")
    print(f"character:{character}")
    print(f"numeric:{numeric}")
count_characters()

#6. Swap first and last characters: Write a python program to swap the first and last characters of a string.
def swap():
    s = input("Enter a string:")
    if len(s) <= 1:
        return s
    swapping = s[-1] + s[1:-1] + s[0]
    print(swapping)  
swap()

#8. Word frequency count: Write a python program to count the occurences of each word in a given sentence.
def occurences():
    sentence = input("Enter a sentence:")
    words = sentence.split()
    word_counts = {}
    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    print(word_counts)
occurences()

#9. Convert to uppercase and lowercase: Write a python program to convert a string to uppercase and lowercase.
def convert():
    s = input("Enter your string:")
    uppercase = s.upper()
    lowercase = s.lower()
    print(f"uppercase:{uppercase}")
    print(f"lowercase:{lowercase}")
convert()