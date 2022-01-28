#перебор всех пар "ключ-значение"

user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)    

#или с короткими однобуквенными именами переменных
for k, v in user_0.items():
	print("\nKey: " + k)
	print("Value: " + v)
	
# items() метод возвращающий список пар "ключ-значение"

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'pivil': 'python',
    }
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is "+
	language.title()+ '.')
	
#перебор всех ключй в словаре
# метод keys() удобен для работы со всеми значения в словаре

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'pivil': 'python',
    }
for name in favorite_languages.keys():
	print(name.title())

#также по умолчанию перебор:
for name in favorite_languages:
	print(name.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'pivil': 'python',
    }
friends = ['pivil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print(" Hi "  + name.title() + 
		", I see your favorite language is " +
		favorite_languages[name].title()+ "!")
		
#проверка ключа в словаре метод keys()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'pivil': 'python',
    }
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

#упорядоченный перебор ключей словаря
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'pivil': 'python',
    }
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

#перебор всех "значений" в словаре метод values()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'pivil': 'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

#множество (set) похоже на список, но все его элементы уникальны

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'pivil': 'python',
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

#упражнение 6-4
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
for key, value in glossary.items():
	print("\nKey: " + key)
	print("Value: " + value)

glossary['developer'] = 'разработчик программного обеспечения'
glossary['library'] = 'сборник подпрограмм или объектов, используемых' \
			'для разработки программного обеспечения'
glossary['Modular programming'] = 'организация программы как ' \
			'совокупности небольших независимых блоков, называемых' \
			'модулями, структура и поведение которых подчиняются ' \
			'определённым правилам'
glossary['computer program'] = 'комбинация компьютерных инструкций ' \
			'и данных, позволяющая аппаратному обеспечению ' \
			' вычислительной системы выполнять вычисления или ' \
			'функции управления'
glossary['Интерпретация'] = 'построчный анализ, обработка и ' \
			'выполнение исходного кода программы или запроса ' \
			'(в отличие от компиляции, где весь текст программы, ' \
			'перед запуском, анализируется и транслируется в машинный '\
			'или байт-код, без её выполнения)'

for key, value in glossary.items():
	print("\nKey: " + key)
	print("Value: " + value)

#упражнение 6-5

rivers = {
	'nile': 'egypt',
	'volga': 'rossia',
	'amazon': 'south america',
	}

for key, value in rivers.items():
	print('\nThe '+ key.title() + " runs through " + value.title())

for river in sorted(rivers.keys()):
	print(river.title())
	
for river in sorted(rivers.values()):
	print(river.title())
	
#упражнение 6-6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'pivil': 'python',
    }

people = [ 
    'jen',
    'sarah',
    'edward',
    'x',
    'pivil',
    'y',
    'z',
    ]
    
for name in people:
	
	if name not in favorite_languages.keys():
		print("\nHi "  + name.title()+ " please take a survey!")
	else:
		print("\nThank you " + name.title())	   



