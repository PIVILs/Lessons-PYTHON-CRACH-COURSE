
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

#упражнение 6-7

person_0 = {
    'name': 'youliya', 
    'surname': 'guskova', 
    'age': '35', 
    'position': 'beauty director',
    'hair color': 'blonde',
	'city': 'samara',
	}

person_1 = {
    'name': 'serge', 
    'surname': 'guskov', 
    'age': '15', 
    'position': 'lyceum student',
    'hair color': 'brown',
	'city': 'samara',
	}

person_2 = {
    'name': 'semen', 
    'surname': 'guskov', 
    'age': '2', 
    'position': 'householder',
    'hair color': 'blonde',
	'city': 'samara',
	}

people = [person_0, person_1, person_2]

for person in people:
    print(person)

#упражнение 6-10

favorite_nambers = {
    'jen': {'one': '5', 'two': '6'},
    'sarah': {'one': '10', 'two': '12'},
    'edward': {'one': '20', 'two': '22'},
    'pivil': {'one': '11', 'two': '07'},
    }

for name, info in favorite_nambers.items():
    print("\nName: " + name)
    favorite_namber = info['one'] + " and " + info['two']
    print(favorite_namber)

