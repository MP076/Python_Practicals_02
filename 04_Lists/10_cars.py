# Organizing a List ---
# Sorting a List Permanently with the sort() Method --
# 75
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)


# Reverse sorting --
# 76
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


# Sorting a List Temporarily with the sorted() Function --
# 77
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)


# Printing a List in Reverse Order --
# 78
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)


# Finding the Length of a List --
# 79
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))


# O/p:
# ['audi', 'bmw', 'subaru', 'toyota']
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
