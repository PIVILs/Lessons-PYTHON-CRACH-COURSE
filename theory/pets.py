#удаление всех вхождений конкретного значения из списка
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#позиционные аргументы

def describe_pet(animal_type, pet_name):
    """Выводит информацию о животном"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster', 'harry')


#многократные вызовы функций

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#о важности порядка позиционных аргументов

describe_pet('harry', 'hamster')

#именованные аргументы   имя-значение

describe_pet(pet_name='harry', animal_type='hamster') # значения по умолчанию 
#должны следовать после параметров, у которых значей по умолчанию нет

#значения по умолчанию

def describe_pet(pet_name, animal_type='dog'):
    """Выводит информацию о животном"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')

#предотвращение ошибок в аргументах

