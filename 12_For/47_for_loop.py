# FOR LOOP ---

# 1. A for loop acts as an iterator in Python, it goes through items that are in a sequence or any other iterable item.
#     for item in object:
#         statements to do stuff

# 2. The variable name used for the item is completely up to the coder,
#    so use your best judgment for choosing a name that makes sense and you will be able to understand when revisiting
#    your code. This item name can then be referenced inside you loop.
#    For example if you wanted to use if statements to perform checks.


# for loop with a list --
# 211
mylist = [1, 2, 3, 4]

for num in mylist:
    print(num)


# 212
# mylist = [1, 2, 3, 4]
#
# for totally_made_up in mylist:
#     print(totally_made_up)


# 213
# mylist = [1, 2, 3, 4]
#
# for num in mylist:
#     print(num, end=' ')


# 214
# mylist = [1, 2, 3, 4]
#
# for num in mylist:
#     print("some unrelated variable, but print for every num in mylist")


# for loop with strings --
# 215
# for letter in "This is a string recruit":
#     print(letter)

# 216
# mystring = 'This is a string recruit'
# for word in mystring.split():
#     print(word)


# for loop with tuple --
# 217
# tup = (1, 2, 3, 4)
#
# for num in tup:
#     print(num)


# tuple unpacking --
# 218
# list_of_tups = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
#
# for x in list_of_tups:
#     print(x)

# 219
# list_of_tups = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
#
# for x in list_of_tups:
#     print(x[0])
# print("\n")
#
# for x in list_of_tups:
#     print(x[1])


# 220
# list_of_tups = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
#
# for (num1, num2) in list_of_tups:
#     print(num1)
#     print(num2)
#     print('\n')


# Doesn't need the parenthesis -
# 221
# list_of_tups = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
#
# for num1, num2 in list_of_tups:
#     print(num1)
#     print(num2)
#     print('\n')


# for loop with dictionaries --
# 222
# my_dictionary = {'a': 1, 'b': 2, 'c': 3}
#
# # Remember that dictionaries don't retain any order! So only loop through them with this in mind!
# for item in my_dictionary:
#     print(item)


# 223
# my_dictionary = {'a': 1, 'b': 2, 'c': 3}
#
# for k in my_dictionary.keys():
#     print(k)


# 224
# my_dictionary = {'a': 1, 'b': 2, 'c': 3}
#
# for k in my_dictionary.keys():
#     print(k)
#     print(my_dictionary[k])
#     print('\n')


# continue --
# a. The continue keyword can be a bit tricky to see its usefulness,
#    but it allows you to continue with the top level loop, basically the opposite of break.
# b. It will take time before you realize a good situation to use it in.

# 225
# for letter in 'code':
#     if letter == 'd':
#         continue
#     print('Current Letter is: {}'.format(letter))


# O/p:
# 1
# 2
# 3
# 4
#
# 1
# 2
# 3
# 4
#
# 1 2 3 4
#
# some unrelated variable, but print for every num in mylist
# some unrelated variable, but print for every num in mylist
# some unrelated variable, but print for every num in mylist
# some unrelated variable, but print for every num in mylist
#
#
# T
# h
# i
# s
#
# i
# s
#
# a
#
# s
# t
# r
# i
# n
# g
#
# r
# e
# c
# r
# u
# i
# t
#
#
# This
# is
# a
# string
# recruit
#
#
# 1
# 2
# 3
# 4
#
#
# (1, 2)
# (3, 4)
# (5, 6)
# (7, 8)
# (9, 10)
#
#
# 1
# 3
# 5
# 7
# 9
#
# 2
# 4
# 6
# 8
# 10
#
#
# 1
# 2
#
# 3
# 4
#
# 5
# 6
#
# 7
# 8
#
# 9
# 10
#
#
# 1
# 2
#
# 3
# 4
#
# 5
# 6
#
# 7
# 8
#
# 9
# 10
#
#
# a
# b
# c
#
#
# a
# b
# c
#
#
# a
# 1
#
# b
# 2
#
# c
# 3
#
#
# Current Letter is: c
# Current Letter is: o
# Current Letter is: e
