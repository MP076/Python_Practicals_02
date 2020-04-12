# Use of range() function in for loop --
# 95
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


# 96
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)


# Simple Statistics with a List of Numbers --
# 97
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


# List Comprehensions --
# 98
squares = [value ** 2 for value in range(1, 11)]
print(squares)


# O/p:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# 0
# 9
# 45
#
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
