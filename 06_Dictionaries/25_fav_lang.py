# # A List in a Dictionary --
# 141
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


# O/p:
# Jen's favorite languages are:
# 	Python
# 	Ruby
#
# Sarah's favorite languages are:
# 	C
#
# Edward's favorite languages are:
# 	Ruby
# 	Go
#
# Phil's favorite languages are:
# 	Python
# 	Haskell
