#Начинаем с двух списков: пользователей для проверки и пустого для хранения проверенных

uncofirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#проверяем каждого пользователя, пока остаются непроверенные пользователи
#Каждый пользователь, порошедший проверку, перемещается в список проверенных

while uncofirmed_users:
    current_user = uncofirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
#вывод всех проверенных пользователей.
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
