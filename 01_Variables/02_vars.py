# Variables ---
# Assigning Var --
# 02
message = "Hello World!"
print(message)


# Reassignment with the same var --
# 03
message = "Hello Python World!"
print(message)

# Another Reassignment example -
# 04
a = 1000
print("a =", a)
a += a
print("a =", a)
a += a
print("a =", a)


# Avoiding Name Errors When Using Variables --
# 05: error
# message = "Hello Python Crash Course reader!"
# print(mesage)
# O/p:
# NameError: name 'mesage' is not defined

# 06
mesage = "Hello Python Crash Course reader!"
print(mesage)
# O/p:
# "Hello Python Crash Course reader!"


# Simple Encryption and Decryption Example -
# 07
message = 111
hash_code = 346728236
secret_message = message * hash_code
print("secret_message:", secret_message)

decrypted_message = secret_message / hash_code
print("decrypted_message:", decrypted_message)


# O/p:
# Hello World!
#
# Hello Python World!
#
# a = 1000
# a = 2000
# a = 4000
#
# Hello Python Crash Course reader!
#
# secret_message: 38486834196
# decrypted_message: 111.0
