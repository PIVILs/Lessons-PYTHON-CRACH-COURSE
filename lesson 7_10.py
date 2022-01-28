
locations = {}

following_user = True

while following_user:
    
    name = input("\nWhat is your name? ")
    location = input("Где хотели бы провести отпуск? ")
    
    
    locations[name] = location
    
    
    repeat = input("Кто еще будет учавствовать в опросе? (yes/ no)")
    if repeat == 'no':
        following_user = False
        

print("\n--- Poll Results ---")
for name, location in locations.items():
    print(name.title() + " еще надеется отдохнуть в " + location + "! Ха-ха))")

