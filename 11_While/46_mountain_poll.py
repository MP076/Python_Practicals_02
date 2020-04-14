# Filling a Dictionary with User Input --

# 210
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary:
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")


# O/p:
# What is your name? Joey
# Which mountain would you like to climb someday? Mt. Everest
# Would you like to let another person respond? (yes/ no) yes
#
# What is your name? Bing
# Which mountain would you like to climb someday? K2
# Would you like to let another person respond? (yes/ no) no
#
# --- Poll Results ---
# Joey would like to climb Mt. Everest.
# Bing would like to climb K2.
