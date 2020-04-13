# Writing Clear Prompts --
# 154
name = input("Please enter your name: ")
print("Hello, " + name + "!")

# 155
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
#
# name = input(prompt)
# print("\nHello, " + name + "!")


# Using int() to Accept Numerical Input --
# 156
# age = input("How old are you? ")
# print(age)
# print(type(age))


# 157: Error
# age = input("How old are you? ")
# print(age >= 18)
# O/p:
# TypeError: '>=' not supported between instances of 'str' and 'int'

# 158
# age = input("How old are you? ")
# age = int(age)
# print(age >= 18)


# O/p:
# Please enter your name: Joey
# Hello, Joey!
#
# If you tell us who you are, we can personalize the messages you see.
# What is your first name? Chandler
#
# Hello, Chandler!
#
#
# How old are you? 23
# 23
# <class 'str'>
#
# How old are you? 23
# True
