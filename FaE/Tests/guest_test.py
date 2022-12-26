guest = input("Hello, who's there? ")
with open('guests', 'w') as file_object:
    file_object.write(guest + "\n")

