"""
Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva uma
classe chamada IceCreamStand que herde da classe Restaurant escrita no
Exercício restaurante. Adicione um atributo chamado flavors que armazene uma 
lista de sabores de sorvete. Escreva um método para mostrar esses sabores. Crie 
uma instância de IceCreamStand e chame esse método.
Admin: Um administrador é um tipo especial de usuário. Escreva uma classe
chamada Admin que herde da classe User escrita no Exercício User. Adicione um atributo 
privileges que armazene uma lista de strings como "can add post", "can delete post"
 "can ban user", e assim por diante. Escreva um método chamado show_privileges() que liste o
conjunto de privilégios de um administrador. Crie uma instância de Admin e chame
seu método.
Privilégios: Escreva uma classe Privileges separada. A classe deve ter um
atributo privileges que armazene uma lista de strings conforme descrita no
Exercício anterior. Transfira o método show_privileges() para essa classe. Crie uma
instância de Privileges como um atributo da classe Admin. Crie uma nova
instância de Admin e use seu método para exibir os privilégios.
Upgrade de bateria: Use a última versão de electric_car.py.
Acrescente um método chamado upgrade_battery() na classe Battery. Esse
método deve verificar a capacidade da bateria e defini-la com 85 se o valor for
diferente. Crie um carro elétrico com uma capacidade de bateria default, chame
get_range() uma vez e, em seguida, chame get_range() uma segunda vez após
fazer um upgrade da bateria. Você deverá ver um aumento na distância que o
carro é capaz de percorrer.
"""

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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolat', 'strawberry', 'cream', 'pistach'] 

    def show_flavors(self):
        print(self.restaurant_name.title() + " has those ice cream flavors:")
        for flavor in self.flavors:
            print("- " + flavor.title())

iceking = IceCreamStand('ice king', 'ice creams')
iceking.describe_restaurant()
iceking.show_flavors()

print('\n')

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

class Admin(User):
    def __init__(self, first_name, last_name,
        username, age, location, gender):
        super().__init__(first_name, last_name, 
            username, age, location, gender)
        self.privilegies = ["can add post", "can undelete post",
            "can ban user", "can remove post", "can unban user"]

    
    def show_privilegies(self):
        print(self.username.title() + " has those privilegies as Admin:")
        for privilegie in self.privilegies:
            print("- " + privilegie)

adm_r = Admin('rene', 'descartes', 'cogito', '25', 'bordeaux', 'male')
adm_r.show_privilegies()

print('\n')

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

class Privilegies():
    def __init__(self, privilegies=["can add post", "can undelete post",
            "can ban user", "can remove post", "can unban user"]):
        self.privilegies = privilegies

    def show_privilegies(self):
        print("This user has those privilegies as Admin:")
        for privilegie in self.privilegies:
            print("- " + privilegie)

class Admin(User):
    def __init__(self, first_name, last_name,
        username, age, location, gender):
        super().__init__(first_name, last_name, 
            username, age, location, gender)
        self.privilegies = Privilegies()

adm_v = Admin('leonardo', 'da Vinci', 'the_scientist', 51, 'veneza', 'male')
adm_v.privilegies.show_privilegies()

print('\n')

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:        
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increament_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank():
        print("Filling the tank with gas...")


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85


class EletricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank():
        print("This car doesn't have a gas tank")

my_tesla = EletricCar('tesla', 'model s', 2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
