# The if-elif-else Chain --
# 182
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")


# 183
# age = 12
#
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# else:
#     price = 10
#
# print("Your admission cost is $" + str(price) + ".")


# Using Multiple elif Blocks --
# 184
# age = 12
#
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# else:
#     price = 5
#
# print("Your admission cost is $" + str(price) + ".")


# 185
# if 2 == 0:
#     print('First condition True')
# elif 2 == 1:
#     print("Second condition True")
# elif 2 == 2:
#     print("Third condition True")
# else:
#     print("None of the above conditions were True")

# 186
# if 2 == 0:
#     print('First condition True')
# elif 2 == 1:
#     print("Second condition True")
# elif 2 == 100:
#     print("Third condition True")
# else:
#     print("None of the above conditions were True")


# Final example -
# 187
# agent_code = 231912
# access = False
#
# if agent_code == 12345:
#     print('Code Reset')
#     print("Please call a supervisor")
# elif agent_code == 231912:
#     print('Welcome Agent')
#     print('Setting Your Access to True')
#     access = True
# else:
#     print("Sorry Wrong Code Supplied")


# Omitting the else Block --
# 188
# age = 12
#
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# elif age >= 65:
#     price = 5
#
# print("Your admission cost is $" + str(price) + ".")


# Other examples -
# Now we can actually start another set of control flow logic here
# 189
# access = False
#
# if access == True:
#     print('Access Granted')
# else:
#     print('Access Denied')


# Take a look at the last set of if/else block, since the variable access itself is a boolean,
# we also could have written it like this:
# 190
# access = False
#
# if access:
#     print("Access Granted")
# else:
#     print("Access Denied")


# O/p:
# Your admission cost is $5.
#
# Your admission cost is $5.
#
# Your admission cost is $5.
#
# Third condition True
#
# None of the above conditions were True
#
# Welcome Agent
# Setting Your Access to True
#
# Your admission cost is $5.
#
# Access Denied
#
# Access Denied
