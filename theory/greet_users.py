#Передача списка

def greet_users(names):
    """Вывод простого приветствия для каждого пользователя в списке."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
        
username = ['hannah', 'ty', 'margot']
greet_users(username)
