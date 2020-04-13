# SETS --

# 1. Sets are an unordered collection of unique elements.
# 2. We can construct them by using the set() function.


# 144
set_1 = set()  # Empty Set
print(set_1)
print(type(set_1))

# 145
x = set()
x.add(1)
print("x =", x)

x.add(2)
print("x =", x)


# Note the curly brackets. This does not indicate a dictionary!
# Although you can draw analogies as a set being a dictionary with only keys.

# We know that a set has only unique entries. So what happens when we try to add something that is already in a set?


# 146
x.add(1)
print("x =", x)  # Notice how it won't place another 1 there.


# We can cast a list with multiple repeat elements to a set to get the unique elements.
# 147
my_list = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
print("my_list =", my_list)
print("set(my_list) =", set(my_list))


# 148
print(set('Mississippi'))


# You can also quickly create a set with just {}
# 149
my_set = {1, 2, 3}
print("my_set =", my_set)
print("type(my_set):", type(my_set))


# O/P:
# set()
# <class 'set'>
#
# x = {1}
# x = {1, 2}
#
# x = {1, 2}
#
# my_list = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# set(my_list) = {1, 2, 3}
#
# {'M', 's', 'p', 'i'}
#
# my_set = {1, 2, 3}
# type(my_set): <class 'set'>
