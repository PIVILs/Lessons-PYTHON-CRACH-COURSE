class Restaurant():
    """Простая модель ресторана"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты name и type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
            
    def describe_restaurant(self):
        """Выводит два атрибута название и тип"""
        print(self.restaurant_name.title() + " " + 
			  self.cuisine_type.title() + " " +
			  str(self.number_served) + " мест")
                
    def open_restaurant(self):
        """Открыт"""
        print(self.restaurant_name.title() + " open!")
                
    def set_number_served(self, number_visitors):
        """Задает кол-во обслуживаемых посетителей"""
        self.number_served = number_visitors
                
    def increment_number_served(self, guests):
        """Увеличивает число гостей"""
        self.number_served += guests
                
class IceCreamStand(Restaurant):
    
    """Предоставляет список сортов мороженого"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['пломбир', 'шоколадное', 'ванильное']
        #self.i = 100
        
    def icecream(self):
        print(self.flavors)    
        
        
restaurant = Restaurant('жигули', 'пивоварня')
restaurant.describe_restaurant()

restaurant.set_number_served(100)
restaurant.describe_restaurant()

restaurant.increment_number_served(100)
restaurant.describe_restaurant()

my_cream = IceCreamStand('жигули', 'пивоварня')
my_cream.describe_restaurant()
my_cream.icecream()
