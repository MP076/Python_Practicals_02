# Looping Through All Key-Value Pairs --
# 129
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")


# Looping Through All the Keys in a Dictionary --
# 130
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())


# 131
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")


# 132
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


# Looping Through a Dictionary’s Keys in Order --
# 133
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


# Looping Through All Values in a Dictionary --
# 134
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


# 135
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


# O/p:
# Jen's favorite language is Python.
# Sarah's favorite language is C.
# Edward's favorite language is Ruby.
# Phil's favorite language is Python.
#
# Jen
# Sarah
# Edward
# Phil
#
# Jen
# Sarah
#  Hi Sarah, I see your favorite language is C!
# Edward
# Phil
#  Hi Phil, I see your favorite language is Python!
#
# Erin, please take our poll!
#
# Edward, thank you for taking the poll.
# Jen, thank you for taking the poll.
# Phil, thank you for taking the poll.
# Sarah, thank you for taking the poll.
#
# The following languages have been mentioned:
# Python
# C
# Ruby
# Java
#
# The following languages have been mentioned:
# Java
# C
# Python
# Ruby
