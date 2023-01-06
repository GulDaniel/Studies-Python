#importanto classes
from Cars import Car

my_other_new_car = Car('audi', 'a4', 2016)
print(my_other_new_car.get_descriptive_name())

my_other_new_car.odometer_reading = 23
my_other_new_car.read_odometer()
