from users_0 import Users
from users_0_1 import Admin

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

