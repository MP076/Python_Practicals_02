# LISTS ---
# 1. Lists are sequences of objects, they can hold a variety of data types in order.
# 2. They follow the same sequence and indexing bracket rules that strings do.
# 3. They can also take in mixed data types.

# 51
list_1 = [1, 2, 3]
print(list_1)

list_2 = [10, 10.5, "str"]
print(list_2)

a = 100
b = 200
c = 300
list_3 = [a, b, c]
print(list_3)

# 52
fruits = ['apple', 'mango', 'banana', 'grapes']
print(fruits)


# Length of the list --
# 53
print(len(fruits))


# Accessing Elements in a List (Indexing and Slicing) --
# 54
list_4 = ['a', 'b', 'c', 'd']
print(list_4)
print(list_4[1])
print(list_4[0:3])

# 55
fruits = ['apple', 'mango', 'banana', 'grapes']
print(fruits[0])

# 56
print(fruits[1])
print(fruits[3])

print(fruits[-2])

# 57
print(fruits[0].upper())

# Changing an element --
# 58
fruits[0] = 'Changed fruit'
print(fruits)


# Duplicate elements
# 59
fruits = ['apple', 'mango', 'banana', 'grapes']
print(fruits * 2)


# Using Individual Values from a List --
# 60
message = "My favorite fruit is " + fruits[1].title() + "."
print(message)


# O/p:
# [1, 2, 3]
# ['a', 'b', 'c']
# [10, 10.5, 'str']
#
# ['apple', 'mango', 'banana', 'grapes']
#
# 4
#
# ['a', 'b', 'c', 'd']
# b
# ['a', 'b', 'c']
#
# apple
#
# mango
# grapes
#
# banana
#
# APPLE
#
# ['Changed fruit', 'mango', 'banana', 'grapes']
#
# ['apple', 'mango', 'banana', 'grapes', 'apple', 'mango', 'banana', 'grapes']
#
# My favorite fruit is Mango.
