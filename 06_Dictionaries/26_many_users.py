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


# Methods --
# 143
code_names = {
    "Obama": 'Renegade',
    "Bush": 'Trailblazer',
    "Reagan": "Rawhide",
    "Ford": "Passkey"
}

print("code_names.keys() =", code_names.keys())
print("code_names.values() =", code_names.values())
print("code_names.items() =", code_names.items())


# O/p:
# Username: einstein
# 	Full name: Albert Einstein
# 	Location: Princeton
#
# Username: mcurie
# 	Full name: Marie Curie
# 	Location: Paris
#
# code_names.keys() = dict_keys(['Obama', 'Bush', 'Reagan', 'Ford'])
# code_names.values() = dict_values(['Renegade', 'Trailblazer', 'Rawhide', 'Passkey'])
# code_names.items() = dict_items([('Obama', 'Renegade'), ('Bush', 'Trailblazer'), ('Reagan', 'Rawhide'),
# ('Ford', 'Passkey')])
