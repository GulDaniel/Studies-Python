import json

filename = 'userfavnumber.json'

try:
    with open(filename) as f_obj:
        fav_number = json.load(f_obj)
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as f_obj:
         json.dump(favorite_number, f_obj)
else:
        print("I know your favorite number, it is " + fav_number)
