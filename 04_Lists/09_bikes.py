# Changing, Adding, and Removing Elements ---
# Modifying Elements in a List --
# 61
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)

bikes[0] = 'ducati'
print(bikes)


# Basic List Methods ---
# Adding Elements to a List --
# Using append() -
# 62
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)

bikes.append('ducati')
print(bikes)


# 63
bikes = []

bikes.append('honda')
bikes.append('yamaha')
bikes.append('suzuki')

print(bikes)


# Using insert() -
# 64
bikes = ['honda', 'yamaha', 'suzuki']

bikes.insert(0, 'ducati')
print(bikes)


# Removing Elements from a List ---
# Using the del Statement --
# 65
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)

del bikes[0]
print(bikes)


# 66
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)

del bikes[1]
print(bikes)


# Using the pop() Method --
# 67
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)

popped_bike = bikes.pop()
print(bikes)
print(popped_bike)


# 68
bikes = ['honda', 'yamaha', 'suzuki']

last_owned = bikes.pop()
print("The last bike I owned was a " + last_owned.title() + ".")


# Popping Items from any Position in a List --
# 69
bikes = ['honda', 'yamaha', 'suzuki']

first_owned = bikes.pop(0)
print('The first bike I owned was a ' + first_owned.title() + '.')


# Removing an Item by Value --
# 70
bikes = ['honda', 'yamaha', 'suzuki', 'ducati']
print(bikes)

bikes.remove('suzuki')
print(bikes)


# 71
bikes = ['honda', 'yamaha', 'suzuki', 'ducati']
print(bikes)

too_expensive = 'ducati'
bikes.remove(too_expensive)
print(bikes)
print("\nA " + too_expensive.title() + " is too expensive for me.")


# Avoiding Index Errors When Working with Lists ---
# 72: Error
# bikes = ['honda', 'yamaha', 'suzuki']
# print(bikes[3])
# O/p:
# IndexError: list index out of range

# So use reverse indexing to get the last element.
# 73
# bikes = ['honda', 'yamaha', 'suzuki']
# print(bikes[-1])

# 74: Error
# bikes = []
# print(bikes[-1])
# O/p:
# IndexError: list index out of range


# O/p:
# ['honda', 'yamaha', 'suzuki']
# ['ducati', 'yamaha', 'suzuki']
#
# ['honda', 'yamaha', 'suzuki']
# ['honda', 'yamaha', 'suzuki', 'ducati']
#
# ['honda', 'yamaha', 'suzuki']
#
# ['ducati', 'honda', 'yamaha', 'suzuki']
#
# ['honda', 'yamaha', 'suzuki']
# ['yamaha', 'suzuki']
#
# ['honda', 'yamaha', 'suzuki']
# ['honda', 'suzuki']
#
# ['honda', 'yamaha', 'suzuki']
# ['honda', 'yamaha']
# suzuki
#
# The last bike I owned was a Suzuki.
#
# The first bike I owned was a Honda.
#
# ['honda', 'yamaha', 'suzuki', 'ducati']
# ['honda', 'yamaha', 'ducati']
#
# ['honda', 'yamaha', 'suzuki', 'ducati']
# ['honda', 'yamaha', 'suzuki']
#
# A Ducati is too expensive for me.
