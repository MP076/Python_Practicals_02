# Organizing a List ---
# Sorting a List Permanently with the sort() Method --
# 75
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)


# Remember, sorting occurs but does not return it --
# 76
cars = ['bmw', 'audi', 'toyota', 'subaru']
sorted_cars = cars.sort()
print(sorted_cars)
print(type(sorted_cars))

# None is a special object used to indicate no value.
# It is the return value of a function/method that does not actually return any value.

# Reverse sorting --
# 77
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


# Sorting a List Temporarily with the sorted() Function --
# 78
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)


# Printing a List in Reverse Order --
# 79
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)


# Finding the Length of a List --
# 80
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))


# Nested List example--
# 81
new_list = [1, 2, 3, ['a', 'b', 'c']]
print("new_list =", new_list)
print("type(new_list): ", type(new_list))
print("new_list[3] =", new_list[3])
print("new_list[3][0] =", new_list[3][0])


# O/p:
# ['audi', 'bmw', 'subaru', 'toyota']
#
# None
# <class 'NoneType'>
#
# ['toyota', 'subaru', 'bmw', 'audi']
#
# Here is the original list:
# ['bmw', 'audi', 'toyota', 'subaru']
#
# Here is the sorted list:
# ['audi', 'bmw', 'subaru', 'toyota']
#
# Here is the original list again:
# ['bmw', 'audi', 'toyota', 'subaru']
#
#
# ['bmw', 'audi', 'toyota', 'subaru']
# ['subaru', 'toyota', 'audi', 'bmw']
#
# 4
#
# new_list = [1, 2, 3, ['a', 'b', 'c']]
# type(new_list):  <class 'list'>
# new_list[3] = ['a', 'b', 'c']
# new_list[3][0] = a
