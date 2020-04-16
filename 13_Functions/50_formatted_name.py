# Return Values ---
# Returning a Simple Value --


# 235
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# Making an Argument Optional --
# 236
# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)


# 237
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
#
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)
