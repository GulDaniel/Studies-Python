while True:
    guest = input("Hello, who's there? ")
    print("Welcome " + guest.title())
    with open('guest_book', 'a') as file_object:
        file_object.write(guest.title() + '\n')
    repeat = input("add another guest? (y/n) ")
    if repeat == 'n':
        break

