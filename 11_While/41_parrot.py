# Letting the User Choose When to Quit --

# 199
passcode = 0

while passcode != 123:
    passcode = int(input("Please provide your passcode: "))
    # This won't run until the while loop is done because of the indentation
print("Correct Passcode!")


# 200
# passcode = 0
#
# while passcode != 123:
#     passcode = int(input("Please provide your passcode: "))
#
#     # Nested control flow logic
#     if passcode != 123:
#         print("Sorry wrong passcode provided")
#         print("Try Again")
#         print('\n')
# # This won't run until the while loop is done because of the indentation
# print("Correct Passcode!")


# 201
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
#
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)


# 202
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#
#     if message != 'quit':
#         print(message)


# Using a Flag --
# 203
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
#
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)


# O/p:
# Please provide your passcode: 234
# Please provide your passcode: 123
# Correct Passcode!
#
#
# Please provide your passcode: 234
# Sorry wrong passcode provided
# Try Again
#
#
# Please provide your passcode: 123
# Correct Passcode!
#
#
# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. Hello!
# Hello!
#
# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. quit
# quit
#
#
# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. Hello
# Hello
#
# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. quit
#
#
# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. Hello
# Hello
#
# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. Hi
# Hi
#
# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. quit
