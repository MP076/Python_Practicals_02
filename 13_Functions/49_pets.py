# Passing Arguments --

# Positional Arguments -


# 228
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')


# Multiple Function Calls -
# 229
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')


# Order Matters in Positional Arguments -
# 230
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet('harry', 'hamster')


# Keyword Arguments -
# 231
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet(animal_type='hamster', pet_name='harry')


# Default Values -
# 232, 233
# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet(pet_name='willie')


# Equivalent Function Calls -
# 233
# # A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')
#
# # A hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')


# Avoiding Argument Errors -
# 234: Error
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet()
# O/p:
# TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
