# 266
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# Importing Multiple Classes from a Module -
# 268
# from car import Car, ElectricCar
#
# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())


# Importing an Entire Module -
# 269
# import car
#
# my_beetle = car.Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())


# Importing All Classes from a Module -
# from car import *


# 270
# from car import Car
# from my_electric_car import ElectricCar
#
# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())
