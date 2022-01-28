#Кортежи(tuples) тотже список, но с неизменняемыми(immutable) элементами
#размеры(dimesions)

dimesions = (200, 50)
print(dimesions[0])
print(dimesions[1])

#перебор всех знвчений в кортеже
for dimesion in dimesions:
    print(dimesion)

#замена кортежа
print("Original dimesions:")
for dimesion in dimesions:
    print(dimesion)

dimesions = (400, 100)
print("\nModified dimesions:")
for dimesion in dimesions:
    print(dimesion)

#упражнение 4-13 шведский стол(Buffet)
buffet = ('яйцо', 'рыба', 'сыр', 'колбаса', 'салат')
for menu in buffet:
    print(menu)

buffet = ('яйцо', 'мясо', 'картошка', 'колбаса', 'салат')
for menu in buffet:
    print(menu)
