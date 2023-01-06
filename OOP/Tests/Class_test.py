class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nRestaurant name: " + self.restaurant_name.title())
        print("Cuisine Type: " + self.cuisine_type.title())

    def open_restaurant(self):
        print("--- The restaurant " +
            self.restaurant_name.title() +
            " is open! Be welcome!")

restaurant = Restaurant('wong', 'chinese')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()

cantina = Restaurant('mama', 'italian')
sushi_bar = Restaurant('yazaku', 'japanese')

cantina.describe_restaurant()
sushi_bar.describe_restaurant()

class User():
    def __init__(self, first_name, last_name, 
        username, age, location, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location
        self.gender = gender

    def describe_user(self):
        print("\nUser: " + self.username.title())
        print('Fist name: ' + self.first_name.title())
        print('Last name: ' + self.last_name.title())
        print('Age: ' + str(self.age))
        print('Locaton: ' + self.location.title())
        print('Gender: ' + self.gender.title())

    def greet_user(self):
        print("Welcome " + self.username.title() + "!")

ae = User('albert', 'einstein', 'ainstein', 
    77, 'princeton', 'male')

mc = User('marie', 'curie', 'murie', 
    30, 'paris', 'female')    
    
isn = User('isac', 'newton', 'nisac',
    28, 'london', 'male')

ae.describe_user()
ae.greet_user()

mc.describe_user()
mc.greet_user()

isn.describe_user()
isn.greet_user()
