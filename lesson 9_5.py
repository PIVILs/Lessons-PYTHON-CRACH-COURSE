class Users():
    """Cоздание пользователя"""
    
    def __init__(self, first_name, last_name, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = 0
        
        
    def deskribe_user(self):
        print(
        "\n" + self.first_name.title() + " " + self.last_name.title()
         + " " + self.location.title() + " " + str(self.age))
        
    def greet_user(self):
        print("\nHi " + self.first_name.title() + "!!!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Login attempts: " + str(self.login_attempts))

    def reset_login_atemp(self):
        self.login_attempts = 0
        print("Login attempts: " + str(self.login_attempts))
        
user = Users('Павел', 'Гуськов', 'самара', 35)
user.deskribe_user()
user.greet_user()
user.increment_login_attempts()
user.reset_login_atemp()

user = Users('Юля', 'Гуськова', 'самара', 35)
user.deskribe_user()
user.greet_user()
user.increment_login_attempts()
user.reset_login_atemp()
