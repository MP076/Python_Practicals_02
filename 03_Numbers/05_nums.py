# Numbers ---
# 1. Integers are whole numbers.
# 2. Float (floating point) numbers are numbers with a decimal point.


# Integers --
# 36
print(100)
print(type(100))


# Floats --
# 37
print(1.2)
print(type(1.2))

print(type(100.0))
print(type(100.))


# Basic Arithmetic --
# Addition -
# 38
print(2 + 3)
print(3 + 1.5 + 4)
print(type(3 + 1.5 + 4))  # Value changes to float. Same for multiplication.

# Subtraction -
# 39
print(10 - 5)
print(5 - 10)

# # Multiplication -
# 40
print(5 * 10)
print(4 * 0.5)

# Division -
# 41
print(3 / 2)
print(1 / 2)
print(1 / 1)

# Floor Division -
# 42
print(7 // 4)  # Truncates decimal
print(7 / 4)

# Modulus / Reminder
# 43
print(7 % 4)
print(25 % 4)

# Absolute Value -
# 44
print(abs(-5))

# Power -
# 45
print(2 ** 3)
print(4 ** 0.5)  # Can be used as to find square root too.
print(4 ** (1/2))

print(3 ** 2)
print(3 ** 3)
print(10 ** 7)

import math
print(math.sqrt(25))


# Order of Precedence -
# 46
print(1 + 2 * 3)
print((1 + 2) * 3)

print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)

print(1 + 2 * 1000 + 1)
print((1 + 2) * (1000 + 1))

print(16 / 4 + 25 / 5)
print(16 / (4 + 25) / 5)

print((100.25 - 50.25) / 2 * 4 + 0.25)
print(1.25 + (5 ** 2 * 8 / 2) - 1)
print(60 + (10 ** 2) / 4 * 7)

# 47
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)

# But be aware that you can sometimes get an arbitrary number of decimal places -
# 48
print(0.1 + 0.2)
print(3 * 0.1)
print(0.1 + 0.2 - 0.3)

# O/p:
# 100
# <class 'int'>
#
# 1.2
# <class 'float'>
# <class 'float'>
# <class 'float'>
#
# 5
# 8.5
# <class 'float'>
#
# 5
# -5
#
# 50
# 2.0
#
# 1.5
# 0.5
# 1.0
#
# 1
# 1.75
#
# 3
# 1
#
# 5
#
# 8
# 2.0
# 2.0
#
# 9
# 27
# 10000000
#
# 5.0
#
# 7
# 9
#
# 44
# 29
# 34
#
# 2002
# 3003
#
# 9.0
# 0.1103448275862069
#
# 100.25
# 100.25
# 235.0
#
# 0.2
# 0.4
# 0.2
# 0.4
#
# 0.30000000000000004
# 0.30000000000000004
# 5.551115123125783e-17
