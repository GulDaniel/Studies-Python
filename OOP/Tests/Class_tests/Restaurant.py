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

