# STRINGS ---
# 1. A string is an ordered sequence of characters.
# 2. Remember the keywords here: characters, ordered and immutable.
# 3. Ordered means that we will be able to use indexing and slicing to grab elements from the string.
# 4. Characters hints at the fact that strings are more flexible than just using the alphabet.
# 5. Comments. Won't show up when you run a script.


# Creating strings --
# 08
print('hello')
print("hello")

# Avoiding Syntax Errors with Strings (Potential Error) --
# 09
# message = 'One of Python's strengths is its diverse community.'
# print(message)
# O/P:
# SyntaxError: invalid syntax

# 10
message = "One of Python's strengths is its diverse community."
print(message)


# Length of a string --
# 11
msg = "Hello World"
print(len(msg))


# Adding Whitespace to Strings with Tabs or Newlines (Escape Sequence) --
# Notice how they both follow the general escape character of backslash.
# 12
print('this is a new line \n notice how this prints')

print('this is a tab \t notice how this prints')

# Other examples:
# 13
print("Python")
print("\tPython")

# 14
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Indexing --
# Indexing starts at 0, so the string hello:
# character:    h    e    l   l   o
# index:        0    1    2   3   4
# You can use square brackets to grab single characters
# 15
word = "hello"
print(word[0])
print(word[3])


# Reverse Indexing --
# Reverse indexing is used commonly to grab the last "chunk" of a sequence.
# character:        h     e     l    l    o
# index:            0     1     2    3    4
# reverse index:    0    -4    -3   -2   -1
# 16
print(word[-1])
print(word[-4])


# Slicing --
# We can grab entire subsections of a string with slice notation.
# This is the notation:
#       [start:stop:step]
#
# Key things to note:
# 1. The starting index directly corresponds to where your slice will start
# 2. The stop index corresponds to where you slice will go up to. It does not include this index character!
# 3. The step size is how many characters you skip as you go grab the next one.

# 17
letters = "abcdefghijk"

print(letters)
print(letters[::])  # Technically valid

print(letters[::-1])  # Reverse the string

print(letters[0:3])  # Notice how 'd' is not included.
print(letters[0:4])

print(letters[3:6])  # To get from d to f
print(letters[-8:-5])

print(letters[3:])  # Exclude first 3 elements
print(letters[:3])  # Get first 3 elements

print(letters[2:7:2])  # Start, Stop and Step

print(letters[::2])
print(letters[::3])


# Immutability --
# 18
# name = "Sam"
# name[0] = "P"
# O/p:
# TypeError: 'str' object does not support item assignment


# Repetition --
# 19
letter = 'a'
print(letter * 5)

word = 'hello '
print(word * 3)


# Combining or Concatenating Strings --
# 20
first_name = "chandler"
last_name = "bing"
full_name = first_name + last_name
print(full_name)  # Notice no space in between

full_name = first_name + " " + last_name
print(full_name)


# Basic built-in String methods --
# Changing Case in a String with Methods --
# 21
message = "Hello python world!"
print(message.upper)  # Notice the output when used without the braces.

print(message.upper())  # To Uppercase
print(message.lower())  # To Lowercase
print(message.title())  # Capitalize

str1 = "This is a string"
print((str1.split('i')))

# Other Examples:
# 22
name = "chandler bing"
print("Hello, " + name.title() + "!")
print(name)  # Notice it does not affect the variable.
name = name.title()  # To make permanent changes
print("Hello, " + name + "!")

# 23
email = "chandler.bing@email.com"
split_it = email.split('@')
print(split_it)
print(type(split_it))
print(split_it[1])


# Stripping Whitespace --
# 24
lang = ' Python '
print(lang.rstrip())  # Removes space at right end.
print(lang.lstrip())  # Removes space at left end.
print(lang.strip())  # Removes space at both ends.


# O/p:
# hello
# hello
#
# One of Python's strengths is its diverse community.
#
# 11
#
# this is a new line
#  notice how this prints
#
# this is a tab 	 notice how this prints
#
# Python
# 	Python
#
# Languages:
# Python
# C
# JavaScript
#
# Languages:
# 	Python
# 	C
# 	JavaScript
#
# h
# l
#
# o
# e
#
# abcdefghijk
# abcdefghijk
#
# kjihgfedcba
#
# abc
# abcd
#
# def
# def
#
# defghijk
#
# abc
#
# ceg
#
# acegik
# adgj
#
# aaaaa
# hello hello hello
#
# chandlerbing
# chandler bing
#
# <built-in method upper of str object at 0x033BF1A0>
# HELLO PYTHON WORLD!
# hello python world!
# Hello Python World!
#
# ['Th', 's ', 's a str', 'ng']
#
# Hello, Chandler Bing!
# chandler bing
# Hello, Chandler Bing!
#
# ['chandler.bing', 'email.com']
# <class 'list'>
# email.com
#
#  Python
# Python
# Python
