# Copying a List --
# 105
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print("\n")


# 106
# my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print("\n")


# # This doesn't work (Potential Error):
# 107
my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


# O/p:
# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake']
#
# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake']
#
#
# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli']
#
# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'ice cream']
#
#
# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
#
# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
