# CONTROL STATEMENTS ---

#   if some_condition:
#       Do Something

# A Simple Example --
# 162
# if 1 < 2:
#     print('One is less than two')


# Notice what happens, the indented block of code only runs when the if condition is True!
# 163
# if 1 > 2:
#     print("One is greater than two")

# 164
# cars = ['audi', 'bmw', 'subaru', 'toyota']
#
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())


# Conditional Tests --
# 165
# car = 'bmw'
# print(car == 'bmw')

# 166
# car = 'audi'
# print(car == 'bmw')


# Ignoring Case When Checking for Equality --
# 84
# car = 'Audi'
# print(car == 'audi')
#
# car = 'Audi'
# print(car.lower() == 'audi')

# 86
car = 'Audi'
print(car.lower() == 'audi')
print(car)  # Notice no changes has happened here.


# O/p:
# One is less than two
#
# Audi
# BMW
# Subaru
# Toyota
#
# True
#
# False
#
# False
#
# True
#
# True
# Audi
