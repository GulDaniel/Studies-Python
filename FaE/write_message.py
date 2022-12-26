filename = 'programming'
#w write, r read, a concat, r+ read write

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file.object.write("I love to make new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

