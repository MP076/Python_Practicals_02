# DICTIONARIES ---

# 1. Most programming languages have what is called a hash table, which is a key-item pairing.
# 2. Under the hood, this allows for faster look up times of objects (at the "cost" of not being able to sort the data),
#    practically it allows for us to store data with a mapping.
# 3. The choice of deciding between sequences like a list and mappings like a dictionary
#    often depends on the specific situation.


# 116
d = {'key1': 'value1', 'key2': 'value2'}
print(d)
print(type(d))


# Accessing Values in a Dictionary (Call values by their key) -
# 117
print(d['key1'])
print(d['key2'])

# 118
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 119
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


# Adding New Key-Value Pairs --
# 120
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# Starting with an Empty Dictionary --
# 121
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


# 1. Dictionaries are unordered!
# 2. This may not be clear at first with smaller dictionaries,
#    but as dictionaries get larger they won't retain order, which means they can not be sorted!
# 3. If you need order and the ability to sort, stick with a sequence, like a list!
# 4. One last time - A DICTIONARY IS AN UNORDERED MAPPING. THIS IS NOT IMMEDIATELY OBVIOUS WITH SMALL DICTIONARIES!


# Modifying Values in a Dictionary --
# 122
d = {'a': 1, 'z': 2}
print(d)

d['new'] = 0
print(d)

d['za'] = 'hello'
print(d)


# 123
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


# Dictionaries are very flexible in the data types they can hold. -
# They can hold numbers, strings, lists, and even other dictionaries!
# 124
d = {'k1': 10, 'k2': 'stringy', 'k3': [1, 2, 3, ], 'k4': {'inside_key': 100}}
print(d)
print(d['k1'])
print(d['k2'])
print(d['k3'])
print(d['k3'][0])
print(d['k4'])
print(d['k4']['inside_key'])


# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
# 125
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))


# Removing Key-Value Pairs --
# 126
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


# O/p:
# {'key1': 'value1', 'key2': 'value2'}
# <class 'dict'>
#
# value1
# value2
#
# green
# 5
#
# You just earned 5 points!
#
# {'color': 'green', 'points': 5}
# {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
#
# {'color': 'green', 'points': 5}
#
# {'a': 1, 'z': 2}
# {'a': 1, 'z': 2, 'new': 0}
# {'a': 1, 'z': 2, 'new': 0, 'za': 'hello'}
#
# The alien is green.
# The alien is now yellow.
#
# {'k1': 10, 'k2': 'stringy', 'k3': [1, 2, 3], 'k4': {'inside_key': 100}}
# 10
# stringy
# [1, 2, 3]
# 1
# {'inside_key': 100}
# 100
#
# Original x-position: 0
# New x-position: 2
#
# {'color': 'green', 'points': 5}
# {'color': 'green'}
