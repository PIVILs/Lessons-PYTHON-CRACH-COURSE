#импортирование классов
#импортирование нескольких классов из модуля
#from car import Car,ElectricCar

#мпортирование модуля в модуль

from car import Car
from electric_car import ElectricCar

my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())


my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_beetle = Car('volksvagen', 'beetle', '2016')
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())


"""
#импортирование всего модуля
#import car

my_beetle = car.Car('volksvagen', 'beetle', '2016')
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())
"""
