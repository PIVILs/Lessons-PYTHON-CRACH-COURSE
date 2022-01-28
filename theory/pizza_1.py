#сохранение информации о заказанной пицце
pizza = {
    'crust': 'thick',
    'toppings': ['mushooms', 'extra cheese'],
    }
    
#Опиание заказа
print("Ypu ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")
    
for topping in pizza['toppings']:
    print("\t" + topping)


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'pivil': ['python'],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language are:")
    else:
        print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print ("\t" + language.title())

#передача произвольного набора аргументов

def make_pizza(*toppings):
    """Вывод списка заказанных дополнений."""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """Выводит описание пиццы."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
        
make_pizza('pepperoni')
make_pizza('mushooms', 'green peppers', 'extra cheese')

#позиционные аргументы с произвольными наборами аргументов

def make_pizza(size, *toppings):
    """Выводит описание пиццы."""
    print("\nMaking a " + str(size) + 
        "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushooms', 'green peppers', 'extra cheese')

