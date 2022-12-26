import json

filename = 'user.json'

def reg_user():
    username = input("Who are you? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)


def greet_user():
    with open(filename) as f_obj:
        username = json.load(f_obj)
    print("Welcome, " + username + "!")


def check_user():
    try: 
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        reg_user() 
        greet_user()
    else:
        confirm = input("Are you " + username + "? (y/n) ")
        if confirm == 'y':
            greet_user()
        else:
            reg_user()
            greet_user()

check_user()

