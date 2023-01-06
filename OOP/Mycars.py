#importando múltiplas classes
from Cars import Car, EletricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = EletricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

#importando modulo completo
#import Cars
#my_beetle = Cars.Car('volkswagen', 'beetle', 2016)
#my_tesla = Cars.EletricCar('tesla', 'roadster', 2016)

#importando todas as classes
#from Cars import *
