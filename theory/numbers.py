# функция range() спектр

for value in range(1,5):
	print(value)

#list() список
numbers = list(range(1,6))
print(numbers)

#построение списка четных чисел
even_numbers = list(range(2,11,2))#последняя цифра приращение
print(even_numbers)

#квадраты целых чисел
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

#более компактный код
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

#статистика с числовыми списками
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits)) #сумма, digits(цифры)

#генератор списка
scuares = [value**2 for value in range(1,11)] #после цикла for не ставят :
print(scuares)

#упражнение
for value in range(1,21):
	print(value)

numbers = list(range(1,1001))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

for value in range(1,21,2):
	print(value) #список нечетный чисел

#список кратных 3
for troika in range(3,31,3):
	troika = list(range(3,31,3))
print(troika)

#кубы
cubes = []
for value in range(1,11):
	cube = value**3
	cubes.append(cube)
print(cubes)

#генератор кубов
cubes = [value**3 for value in range(1,11)]
print(cubes)
