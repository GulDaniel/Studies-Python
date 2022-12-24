cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'Audi'
car.lower() == 'audi'
#True

#verificando diferença
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")


age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
#False
age_0 >= 21 or age_1 >= 21
#True

age_1 = 22
age_0 >= 21 and age_1 >= 21
#True
age_0 >= 21 or age_1 >= 21
#False

#verificando se um valor está na lista
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
#True
'pepperoni' in requested_toppings
#False

#verificando se um valor não está na lista
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response")

#booleans
game_active = True
can_edit = False

age = 19
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")
