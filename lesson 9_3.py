class Users():
    """Cоздание пользователя"""
    
    def __init__(self, first_name, last_name, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        
    def deskribe_user(self):
        print(
        "\n" + self.first_name.title() + " " + self.last_name.title()
         + " " + self.location.title() + " " + str(self.age))
        
    def greet_user(self):
        print("\nHi " + self.first_name.title() + "!!!")
        
        
user = Users('Павел', 'Гуськов', 'самара', 34)
user.deskribe_user()
user.greet_user()

user = Users('Юля', 'Гуськова', 'самара', 35)
user.deskribe_user()
user.greet_user()
