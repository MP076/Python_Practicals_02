# Using break to Exit a Loop --

# 205
x = 0

while x < 10:
    print(x)
    print('add one to x')
    x += 1

    if x == 3:
        # This will cause to break out of the top loop
        # Note that if statements don't count as loops
        break


# 206
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")


# O/p:
# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished.) Italy
# I'd love to go to Italy!
#
# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished.) quit
#
#
