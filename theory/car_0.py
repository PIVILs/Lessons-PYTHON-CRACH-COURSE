
class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное оисание."""
        long_name = str(self.year) + ' ' + self.model + ' ' + self.make
        return long_name.title()
        
    def read_odometer(self):
        """"Выводит пробег машины в милях"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Устанавливает заданное значение на одометре.
        При попытке обратной подкрутки изменение отклоняется.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """Увеличивает показания с заданным приращением"""
        self.odometer_reading += miles
        
        
my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())

#Прямое изменение значения отрибута
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Изменение значения атрибута с помощью метода
my_new_car.update_odometer(25)
my_new_car.read_odometer()

#Изменение значения атрибута с приращением

my_new_car = Car('subaru', 'outback', '2013')
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()
