
import json

favorite_number = input('Favorite number? ')

number = 'Favorite_number.json'

with open(number, 'w') as f_obj:
    json.dump(favorite_number, f_obj)

with open(number) as f_obj:
    number = json.load(f_obj)

print("I know your favorite number: " + number)
