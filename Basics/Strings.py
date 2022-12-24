#comentários

"""
comentário de múltiplas linhas
"""

#Atribuindo valores
message = "Hello, World!"
print(message)

#Título, MAIÚSCULO, minúsculo,
message = "hello, world!"
print(message.title())
print(message.upper())
print(message.lower())

#Concatenando strings
first_message = "Hello"
last_message = "World"
full_message = first_message + " " + last_message
print(full_message)

#Removendo espaços
favorite_language = "python   "
print(favorite_language.rstrip())
favorite_language = "   python"
print(favorite_language.lstrip())
favorite_language = "   python   "
print(favorite_language.strip())

#Concatenando números
age = 23
message = "Happy " + str(age) + "rd birthday!"
print(message)
