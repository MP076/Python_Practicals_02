# A Dictionary in a Dictionary --
# 142
users = {
    'einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


# O/p:
# Username: einstein
# 	Full name: Albert Einstein
# 	Location: Princeton
#
# Username: mcurie
# 	Full name: Marie Curie
# 	Location: Paris

