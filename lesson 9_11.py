import users

user = users.Users('Павел', 'Гуськов', 'самара', 35)
user.deskribe_user()
user.greet_user()
user.increment_login_attempts()
user.reset_login_atemp()
admin = users.Admin('Павел', 'Гуськов', 'самара', 35)

admin.i.show_privileges()

user = users.Users('Юля', 'Гуськова', 'самара', 35)
user.deskribe_user()
user.greet_user()
user.increment_login_attempts()
user.reset_login_atemp()



