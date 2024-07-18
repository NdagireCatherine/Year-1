#LISTS#
#7. Write a python program to remove duplicates from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
unique_numbers = list(set(numbers))
print(unique_numbers)


#8. Write a python program to check if a list is empty or not.
def empty():
    lst = input("Enter a list whether empty or not:")
    if len(lst) == 0:
        print("Is empty.")
    else:
        print("Is not empty.")
empty()
    
#9. Write a python program to clone or copy a list.
def clone(lst):
    return lst.copy()
original_lst = [1, 2, 3, 4]
cloned_lst = clone(original_lst)
print("Original list:", original_lst)
print("Cloned list", cloned_lst)


#10. Write a python program to find the list of words that are longer than n from a given list of words.
def long_words(lst, n):
    words = [word for word in lst if len(word) > n]
    return words
words_lst = ["donkey", "cat", "elephant", "monkey"]
n = 6
print("Words longer than", n, "characters:")
print(long_words(words_lst, n))


#11. Write a python function that takes two lists and returns true if they have atleast one common member.
def common_member():
    list1 = input("Enter your first list:")
    list2 = input("Enter your second list:")
    if len(set(list1) & set(list2)) > 0:
        print("Lists have a common member")
    else:
        print("Lists have no common member.")
common_member()


#12. Write a python program to print a specified list after removing the 0th, 4th and 5th elements.
def remove_elements():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst.pop(0)
    lst.pop(4)
    lst.pop(5)
    print(lst)
remove_elements()

#15. Write a python program to shuffle and print a specified list.
import random
my_list = [3, 4, 5, 6, 7, 8, 9]
shuffled = random.shuffle(my_list)
print("Shuffled list:", my_list)

#19. Write a python program to calculate the difference between the two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 8, 9, 0]
diff = set(list1) - set(list2)
print(diff)

#20. Write a python program to convert a list of characters into a string.
characters = ['C', 'h', 'o', 'c', 'o', 'l', 'a', 't', 'e']
string = ''.join(characters)
print("String:", string)


#23. Write a python program to select an item randomly from a list.
import random
list = [1, 2, 3, 4, 5, 6, 7, 8]
selected_item = random.choice(list)
print(selected_item)


#DICTIONARIES#
#2. Write a python script to add a key to a dictionary.
dict = {'grapes':5, 'pineapple':3, 'mango':2}
dict['watermelon'] = 6
print(dict)

#3. Write a python script to check whether a given key already exists in a dictionary.
def exists(lst, key):
    return key in lst
my_dict = {'apple':5, 'banana':2, 'cocoa':3}
check = 'pineapple'
if exists(my_dict, check):
    print("Key exists in dictionary")
else:
    print("Key doesn't exist in dictionary.")


#TUPLES#
#1. Write a python program to create a tuple.
tuple = (1, 2, 3, 4, 5)
print(tuple)

#2. Write a python program to create a tuple with different data types.
diff_data_types =("beauty", 12, 6.7, True)
print(diff_data_types)


#SETS#
#14. Write a python program to find the maximum and minimum values in a set.
set_values = {20, 21, 19, 23, 25}
max_value = max(set_values)
min_value = min(set_values)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

#15. Write a python program to find the length of a set.
set_values = {20, 23, 16, 19, 67}
set_lnth = len(set_values)
print("Length of the set:", set_lnth)
