
import json

number = 'Favorite_number.json'

try:
    with open(number) as f_obj:
        number = json.load(f_obj)
    
except FileNotFoundError:
    favorite_number = input('Favorite number? ')
    with open(number, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
    print("Now I know your favorite number!")
else:
    print("I know your favorite number: " + number)
