class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\nRestaurant name: " + self.restaurant_name.title())
        print("Cuisine Type: " + self.cuisine_type.title())

    def open_restaurant(self):
        print("--- The restaurant " +
            self.restaurant_name.title() +
            " is open! Be welcome!")

    def set_number_served(self, served_clients):
        if served_clients >= self.number_served:
            self.number_served = served_clients
        else:
            print("Invalid number of served clients")

    def increment_number_served(self, served_clients):
        self.number_served += served_clients

restaurant = Restaurant('Wong', 'chinese')
print("Served clients: " + str(restaurant.number_served))
restaurant.number_served = 5
print("Served clients: " + str(restaurant.number_served))
restaurant.set_number_served(4)
restaurant.set_number_served(7)
print("Served clients: " + str(restaurant.number_served))
restaurant.increment_number_served(14)
print("Served clients: " + str(restaurant.number_served))


class User():
    def __init__(self, first_name, last_name, 
        username, age, location, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print("\nUser: " + self.username.title())
        print('Fist name: ' + self.first_name.title())
        print('Last name: ' + self.last_name.title())
        print('Age: ' + str(self.age))
        print('Locaton: ' + self.location.title())
        print('Gender: ' + self.gender.title())

    def greet_user(self):
        print("Welcome " + self.username.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

vb = User('wernher', 'von braun', 'rocket_father', 33, 'berlim', 'male')
vb.increment_login_attempts() 
vb.increment_login_attempts()
vb.increment_login_attempts()
vb.increment_login_attempts()
vb.increment_login_attempts()
vb.increment_login_attempts()
vb.increment_login_attempts()
vb.increment_login_attempts()
vb.increment_login_attempts()

print(vb.username.title() + ' login attempts: ' + str(vb.login_attempts))
vb.reset_login_attempts()
print(vb.username.title() + ' login attempts: ' + str(vb.login_attempts))
