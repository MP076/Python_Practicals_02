# Print Formatting --
# Also known as String Interpolation.
# Essentially inserting variables when printing a string.
# Achieved using:
# 1. .format() method
# 2. f-string (formatted string literals)(new and better to use.)(3.6 and higher versions)
# 3. placeholders (using '%' character, known as string formatting operator)(old)


# Formatting using .format() method --
# 25
print("Welcome {}".format("Ross"))
name = "Ross"
print("Welcome {}".format(name))

place = "Bangalore"
print("Hello {}! Welcome to {}.".format(name, place))  # By index value order.

print("Hello {1}! Welcome to {0}.".format(name, place))  # Change of index values.
print("Hello {1}! Welcome to {1}.".format(name, place))

print("Hello {a}! Welcome to {b}.".format(a=name, b=place))  # By key value.
print("Hello {a}! Welcome to {a}.".format(a=name, b=place))


# Formatted String literals(f-string) --
# 26
name = "Bing"
place = "Chennai"
print(f"Hello {name}! Welcome to {place}.")


# Formatting using placeholders --
# 27
name = "Joey"
print("Hello %s" % name)

place = "Pune"
print("Hello %s! Welcome to %s" % (name, place))


# Format conversion method --
# %s and %r - Converts Python object to a string using str() and repr() methods.
# 28
print("Hello %s" % 'Joey')
print("Hello %r" % 'Joey')

print("Hello %s" % '\tJoey')
print("Hello %r" % '\tJoey')

# 29
print("Value is %s" % 3.75)
print("Value is %d" % 3.75)


# Multiple Formatting --
# 30
print("First: %s, Second: %5.2f, Third: %r" % ('Hi', 3.1415, 'Bye!'))  # Notice two spaces extra for float value.


# Alignment, Padding and Precision --
# 31
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apple', '3'))
print('{0:8} | {1:9}'.format('Orange', '10'))

# Another example:
# 32
print('{0:<8} | {1:^8} | {2:>8}'.format('Left', 'Center', 'Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format('01', '02', '03'))

# 33
print("{0:=<8} | {1:-^8} | {2:+>8}".format('01', '02', '03'))  # Notice the difference from above example(32)


# Float formatting --
#       {value:width.precision f}
# 34
num = 123.6789
print(num)
print("The code is: {}".format(num))
print("The code is: {:.1f}".format(num))
print("The code is: {:.2f}".format(num))
print("The code is: {:.3f}".format(num))
print("The code is: {:.4f}".format(num))

# Other example:
# 35
result = 100/777
print(result)
print("{r:1.3f}".format(r=result))
print("{r:10.3f}".format(r=result))
print("{r:10.5f}".format(r=result))


# O/p:
# Hello Joey
#
# Welcome Ross
# Welcome Ross
#
# Hello Joey! Welcome to Bangalore.
#
# Hello Bangalore! Welcome to Ross.
# Hello Bangalore! Welcome to Bangalore.
#
# Hello Ross! Welcome to Bangalore.
# Hello Ross! Welcome to Ross.
#
# Hello Bing! Welcome to Chennai.
#
# Hello Joey
#
# Hello Joey! Welcome to Pune
#
# Hello Joey
# Hello 'Joey'
#
# Hello 	Joey
# Hello '\tJoey'
#
# Value is 3.75
# Value is 3
#
# First: Hi, Second:  3.14, Third: 'Bye!'
#
# Fruit    | Quantity
# Apple    | 3
# Orange   | 10
#
# Left     |  Center  |    Right
# 01       |    02    |       03
# 01====== | ---02--- | ++++++03
#
# 123.6789
# The code is: 123.6789
# The code is: 123.7
# The code is: 123.68
# The code is: 123.679
# The code is: 123.6789
#
# 0.1287001287001287
# 0.129
#      0.129
#    0.12870
