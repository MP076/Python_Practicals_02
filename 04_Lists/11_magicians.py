# Looping Through an Entire List ---
# 82
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


# Doing More Work Within a for Loop --
# 83
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

# 84
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")


# Doing Something After a for Loop --
# 85
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")


# Forgetting to Indent --
# 86: Error
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)
# O/p:
# IndentationError: expected an indented block


# Forgetting to Indent Additional Lines (Potential Errors) --
# 87
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")


# Indenting Unnecessarily (hello_world.py)--
# 88: Error
# message = "Hello Python world!"
#     print(message)
# O/p:
# IndentationError: unexpected indent


# Indenting Unnecessarily After the Loop (Potential Errors)--
# 89
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you everyone, that was a great magic show!")


# Forgetting the Colon --
# 90: Error
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians
#     print(magician)
# O/p:
# SyntaxError: invalid syntax


# O/p:
# alice
# david
# carolina
#
# Alice, that was a great trick!
# David, that was a great trick!
# Carolina, that was a great trick!
#
# Alice, that was a great trick!
# I can't wait to see your next trick, Alice.
#
# David, that was a great trick!
# I can't wait to see your next trick, David.
#
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.
#
#
# Alice, that was a great trick!
# I can't wait to see your next trick, Alice.
#
# David, that was a great trick!
# I can't wait to see your next trick, David.
#
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.
#
# Thank you, everyone. That was a great magic show!
#
#
# Alice, that was a great trick!
# David, that was a great trick!
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.
#
# lice, that was a great trick!
# I can't wait to see your next trick, Alice.
#
# Thank you everyone, that was a great magic show!
# David, that was a great trick!
# I can't wait to see your next trick, David.
#
# Thank you everyone, that was a great magic show!
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.
#
# Thank you everyone, that was a great magic show!
