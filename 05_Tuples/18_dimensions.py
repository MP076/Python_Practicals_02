# TUPLES

# 1. Tuples are ordered sequences just like a list, but have one major difference, they are immutable.
# 2. Meaning you can not mutate them, mutate being another word for change.
# 3. It means that you can not reassign in item once its in the tuple, unlike a list, where you can do a reassignment.


# 108
t = (1, 2, 3)
print(type(t))


# Mixed data types are fine --
# 109
t = ('a', 1)
print(t[0])  # Indexing works just like a list.


# Immutability --
# 110
mylist = [1, 2, 3]
print(mylist)
print(type(mylist))

mylist[0] = 'new'  # No problem in making changes to a list. But to a tuple: Error.
print(mylist)

t = (1, 2, 3)
# t[0] = 'new'
# TypeError: 'tuple' object does not support item assignment
#
# t.append('NOPE!')
# AttributeError: 'tuple' object has no attribute 'append'


# Accessing a Tuple --
# 111
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 112: Error
# dimensions = (200, 50)
# dimensions[0] = 250
# O/p:
# TypeError: 'tuple' object does not support item assignment


# Looping Through All Values in a Tuple --
# 113
dimensions = (200, 50, 150)
for dimension in dimensions:
    print(dimension)


# Writing over a Tuple (Overwriting)--
# 114
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


# Tuples Methods --
# 115
t = ('a', 'b', 'c', 'a')
print(t)

print(t.index('b'))  # Returns index of first instance!
print(t.count('a'))  # Counts number of characters.


# Why use tuples?
# 1. Lists and tuples are very similar, so you may find yourself exchanging use cases for either one.
# 2. However, you should use a tuple for collections or sequences that shouldn't be changed,
#   such as the dates of the year, or user information such as an address, street, city, etc.
# 3. One interesting use of tuples involves for loops, we'll cover this later on when we discuss tuple unpacking.


# O/p:
# <class 'tuple'>
#
# a
#
# [1, 2, 3]
# <class 'list'>
# ['new', 2, 3]
#
# 200
# 50
#
# 200
# 50
# 150
#
# Original dimensions:
# 200
# 50
#
# Modified dimensions:
# 400
# 100
#
#
# ('a', 'b', 'c', 'a')
# 1
# 2
