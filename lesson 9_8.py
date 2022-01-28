
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
        

class Privileges():
     
    def __init__(self, privilege=[]):         
        self.privilege = [
			'разрешено добавлять сообщения', 
			'разрешено удалять пользователей', 
			'разрещено банить'
			]
        
    def show_privileges(self):
        print(self.privilege)
        
                
class Admin(Users):
    
    """Особая разновидность пользователя"""
    def __init__(self, first_name, last_name, location, age):
        super().__init__(first_name, last_name, location, age)
        self.i = Privileges()
        
        

               
user = Users('Павел', 'Гуськов', 'самара', 35)
user.deskribe_user()
user.greet_user()
user.increment_login_attempts()
user.reset_login_atemp()
admin = Admin('Павел', 'Гуськов', 'самара', 35)

admin.i.show_privileges()

user = Users('Юля', 'Гуськова', 'самара', 35)
user.deskribe_user()
user.greet_user()
user.increment_login_attempts()
user.reset_login_atemp()


