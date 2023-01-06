from Car import Car
from EletricCar import EletricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
my_tesla = EletricCar('tesla', 'roadster', 2016)

print(my_beetle.get_descriptive_name())
print(my_tesla.get_descriptive_name())
