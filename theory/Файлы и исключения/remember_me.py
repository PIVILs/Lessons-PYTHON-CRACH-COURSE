
import json

# Программа загружает имя пользователя, если оно было сохранено ранее.
# Впротивном случае она запрашивает имя пользователя и сохраняет его.

def get_stored_username():
    """Получает хранимое имя пользователя, если оно уже существует."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
        
def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("Wat is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
            
def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    print("Hi! You " + username + "?")
    a = input('\ny or n?\n')
    #if username:
    if a == 'y':
        print('\nHi, '+ username + '!')
        print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("Hello to you too, " + username + "!")
        

greet_user()
