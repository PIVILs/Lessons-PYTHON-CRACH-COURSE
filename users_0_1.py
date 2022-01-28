from users_0 import Users

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
