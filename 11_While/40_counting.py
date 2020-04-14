# WHILE LOOP ---

# A while loop will repeatedly execute a single statement or group of statements
# as long as the condition being checked is true.


# 197
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1


# 198
# x = 0
#
# while x < 3:
#     print('X is currently', x)
#     print("Adding 1 to x")
#     x += 1  # alternatively you could write x = x + 1


# Cautionary Note!
# Be careful with while loops! There is a potential to write a condition that always remains True,
# meaning you have an infinite running while loop. If this happens to you, try using Ctrl+C to kill the loop.


# O/p:
# 1
# 2
# 3
# 4
# 5
#
# X is currently 0
# Adding 1 to x
# X is currently 1
# Adding 1 to x
# X is currently 2
# Adding 1 to x
