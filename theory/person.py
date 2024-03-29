#Возвращение словаря

def build_person(first_name, last_name):
    """Возвращает словарь с инормацией о человеке"""
    person = {'first': first_name, 'last': last_name}
    return person
    
musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age =' '):
    """Возвращает словарь с инормацией о человеке"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
    
musician = build_person('jimi', 'hendrix', age=34)
print(musician)
