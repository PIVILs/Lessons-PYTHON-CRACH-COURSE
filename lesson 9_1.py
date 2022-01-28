class Restaurant():
    """Простая модель ресторана"""
    
    
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты name и type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    
    def describe_restaurant(self):
        """Выводит два атрибута название и тип"""
        print(self.restaurant_name.title() + " " + self.cuisine_type.title())
    def open_restaurant(self):
        """Открыт"""
        print(self.restaurant_name.title() + " open!")
        
restaurant = Restaurant('жигули', 'пивоварня')
print(restaurant.restaurant_name, restaurant.cuisine_type) 

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1 = Restaurant('у швейка', 'пивоварня')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('максимилианс', 'пивоварня')
restaurant_2.describe_restaurant()
