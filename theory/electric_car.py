#наследование
from car import Car

class Battery():
    """Простая модель аккумулятора электромобиля."""
    
    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Выводит информацию о мощности акб."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def get_range(self):
        """Выводит приблизительный запас хода для акб."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
              
    def fill_gas_tank(self):
        """У электромобиля нет бензобака."""
        print("This car doesn't neet a gas tank!")
        
my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
