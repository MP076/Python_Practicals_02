# Using the range() Function --
# 91
for value in range(1, 5):
    print(value)  # It is within 1 to 5, so 5 its excluded.
print("\n")

# 92
for value in range(1, 6):
    print(value)
print("\n")


# Using range() to Make a List of Numbers --
# 93
numbers = list(range(1, 6))
print(numbers)
print("\n")

# 94
even_numbers = list(range(2, 11, 2))
print(even_numbers)


# O/p:
# 1
# 2
# 3
# 4
#
# 1
# 2
# 3
# 4
# 5
#
# [1, 2, 3, 4, 5]
#
# [2, 4, 6, 8, 10]
