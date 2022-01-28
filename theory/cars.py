#метод sort() сортирует список по алфавиту
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#по алфавиту в обратном порядке
cars.sort(reverse=True)
print(cars)

#функция sorted() позволяет представить список в определенном порядке, но не изменяет фактического порядка элементов в списке
#ВАЖНО! После вызова функции sorted() список продолжает находиться в исходном порядке
#только для строчного регистра

cars = ['bmw','audi','toyota','subaru']
print(cars)

print("\n Here i the original list:")
print(cars)

print("\n Here i the sorted list:")
print(sorted(cars))

print("\n Here i the original list again:")
print(cars)

#метод reverse() для перестановки списка в обратном порядке, постоянное изменение

cars.reverse()
print(cars)

#функция len() определение длины списка


print(len(cars))

#упражнения. Страны. country

country = ['китай','япония','италия','бразилия','сша']
print(country)
print(sorted(country))
print(country)
print(sorted(country, reverse=True)) #!!!
print(country)
country.reverse()
print(country)
country.reverse()
print(country)
country.sort()
print(country)
country.reverse()
print(country)
print(len(country)) #функция len() определяет длину списка
