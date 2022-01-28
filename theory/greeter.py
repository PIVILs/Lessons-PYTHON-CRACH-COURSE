prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhath is your first name? "

name = input(prompt)
print("\nHello, " + name.title() + "!")

#определение функции
def greet_user():
    """Выводит простое приветствие"""
    print("Hello!")

greet_user()

#передача информации функции
def greet_user(username):
    """Выводит простое приветствие"""
    print("Hello, " + username.title() + "!")

greet_user('Pool')

