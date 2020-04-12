# Slicing a List --
# 99
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 100
print(players[1:4])

# 101
print(players[:4])

# 102
print(players[2:])

# 103
print(players[-3:])


# Looping Through a Slice --
# 104
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


# O/p:
# ['charles', 'martina', 'michael']
#
# ['martina', 'michael', 'florence']
#
# ['charles', 'martina', 'michael', 'florence']
#
# ['michael', 'florence', 'eli']
#
# ['michael', 'florence', 'eli']
#
# Here are the first three players on my team:
# Charles
# Martina
# Michael
