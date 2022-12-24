def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user('Jesse')

def fav_book(title):
    print('My favorite book is ' + title.title() + ".")

title = 'die leiden des jungen werther'
fav_book(title)

#argumentos posicionais
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#argumentos nomeados
describe_pet(animal_type='hamster', pet_name='harry')

#default
#argumentos default devem vir por último
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('willie')

#dog willie
#describe_pet(animal_type='dog', pet_name='willie')
#describe_pet('willie')
##describe_pet(pet_name='willie')

#hamster harry
#describe_pet('harry', 'hamster')
#describe_pet(pet_name='harry', 'animal_type='hamster')
#describe_pet('harry', animal_type='hamster'

