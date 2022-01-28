#глава 6 словари "ключ-значение"
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#добавление новых пар "ключ-значение"
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#создание пустого словаря
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#изменение значений в словаре
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + "." )

alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'] + "." )

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original x-position: " + str(alien_0['x_position']))
#пришелец перемещается в право.
#вычисляем величину смещения на основании текущей скорости.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #пришелец двигается быстро
    x_increment = 3
#новая позиция равна сумме старой и приращения

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#удаление НАВСЕГДА пар "ключ-значение"
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

#словарь с однотипными объектами
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'pivil': 'python',
    }
print("Pivil's favorite languages is " +
    favorite_languages['pivil'].title() +
    ".")

#упражнение 6-1
person = {
    'name': 'youliya', 
    'surname': 'guskova', 
    'age': '34', 
    'position': 'beauty director',
    'hair color': 'blonde',
	'city': 'samara',
	}
print("My wife " + person['name'].title() + " " \
		+ person['surname'].title() \
		+ " at age " + person['age'] \
		+ " working in positions " + person['position'] \
		)

#упражнение 6-2
favorite_nambers = {
    'jen': '5',
    'sarah': '2',
    'edward': '777',
    'pivil': '11',
    }
print("Jen's favorite number " + str(favorite_nambers['jen']))
print("Sarah's favorite number " + str(favorite_nambers['sarah']))
print("Edward's favorite number " + str(favorite_nambers['edward']))
print("PIVIL's favorite number " + str(favorite_nambers['pivil']))

#упражнение 6-3
glossary = {
    'concatenation': '\nоперация склеивания объектов линейной структуры ',
    'framework': '\nзаготовки, шаблоны для программной платформы ',
    'development environment': '\nИнтегрированная среда разработки, ИСP '\
			'также единая среда разработки, ЕСР — комплекс программных средств ,'\
			'используемый программистами для разработки программного '\
			'обеспечения (ПО)',
	'Compiler': '\nпрограмма или техническое средство, выполняющее ' \
			'компиляцию',
	'Source': '\nтекст компьютерной программы на каком-либо языке ' \
			'программирования или языке разметки,' \
			'который может быть прочтён человеком'
    }
print("Конкатенация: " + glossary['concatenation'])
print("Фреймворк: " + glossary['framework'])
print("Среда разработки: " + glossary['development environment'])
print("Компилятор: " + glossary['Compiler'])
print("Исходный код: " + glossary['Source'])




