# Avoiding Type Errors with the str() Function --
# 49
# age = 23
# message = "Happy " + age + "rd Birthday!"
# print(message)
# O/p:
# TypeError: can only concatenate str (not "int") to str

# 50
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
