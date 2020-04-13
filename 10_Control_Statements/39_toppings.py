# Testing Multiple Conditions
# 191
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")


# 104
# requested_toppings = ['mushrooms', 'extra cheese']
#
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# elif 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# elif 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
#
# print("\nFinished making your pizza!")


# Checking for Special Items --
# 105
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     print("Adding " + requested_topping + ".")
#
# print("\nFinished making your pizza!")


# 106
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print("Adding " + requested_topping + ".")
#
# print("\nFinished making your pizza!")


# Checking That a List Is Not Empty --
# 107
# requested_toppings = []
#
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print("Adding " + requested_topping + ".")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")


# Using Multiple Lists --
# 108
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
#
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + ".")
#     else:
#         print("Sorry, we don't have " + requested_topping + ".")
#
# print("\nFinished making your pizza!")


# O/p:
# Adding mushrooms.
# Adding extra cheese.
#
# Finished making your pizza!
#
#
# Adding mushrooms.
#
# Finished making your pizza!
#
#
# Adding mushrooms.
# Adding green peppers.
# Adding extra cheese.
#
# Finished making your pizza!
#
#
# Adding mushrooms.
# Sorry, we are out of green peppers right now.
# Adding extra cheese.
#
# Finished making your pizza!
#
#
# Are you sure you want a plain pizza?
#
#
# Adding mushrooms.
# Sorry, we don't have french fries.
# Adding extra cheese.
#
# Finished making your pizza!
