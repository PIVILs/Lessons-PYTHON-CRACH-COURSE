#срезы (slices)

players = ['charles', 'martina', 'florence', 'eli']
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

#от начала списка
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

#конец списка
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

#три последних, будет работать даже при изменении списка
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

#цикл for для перебора содержимого списка
print("Here are the first three players on my team:")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[0:3]:
	print(player.title())

#копирование списка
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend favorite foods are:")
print(friend_foods)

#упражнения 4-10
animals = ['dog', 'cat', 'goose', 'deer', 'bear']
print("\n\nThe first three items in the are:")
print(animals[:3])
print("\nThe items from the middle of the list are:")
print(animals[1:4])
print("\nThe last three items in the list are:")
print(animals[2:])

#4-11
pizzas = ['примавера', 'грибная', 'четыресыра']
friend_pizzas = pizzas[:]
pizzas.append('мясная')
friend_pizzas.append('морепродукты')
print(pizzas)
print(friend_pizzas)

for pizza in pizzas:
	print("My favorite pizzas are: "+pizza.title())
	
for friend_pizza in friend_pizzas:
	print("My friend's favorite pizzas are: "+friend_pizza.title())

#4-12
for friend_food in friend_foods[:]:
	print(friend_food.title())
