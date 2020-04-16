# Storing Your Functions in Modules --
# Importing an Entire Module -


# 249
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


# Styling Functions --
# def function_name(parameter_0, parameter_1='default value')

# function_name(value_0, parameter_1='value')

# def function_name(
#         parameter_0, parameter_1, parameter_2,
#         parameter_3, parameter_4, parameter_5):
#     function body...
