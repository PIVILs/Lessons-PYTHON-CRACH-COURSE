#простейшие команды if    voting(голосование)
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#команды if-else
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#цепочки if-elif-else      amusement_park.py парк развлечений
age = 18
if age <= 4:
    print("Your admission cost 0$.")
elif age < 18:
    print("Your admission cost 5$.")
else:
    print("Your admission cost 10$.")

age = 30
if age <= 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")
#без else

age = 65
if age <= 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")

#проверка нескольких условий
#Если нужно чтобы в программе выполнялось только одно условие то if-elif-else
#Если несколько условий , то используют серию независимых команд if

#упражнение 5-3
alien_color = 'yellow'
if alien_color == 'yellow':
    print("Ты только что заработал 5 очков")
if alien_color == 'green':
    print("Ты только что заработал 5 очков")

#упражнение 5-4
alien_color = 'yellow'
if alien_color == 'green':
    print("Ты только что заработал 5 очков")
else:
    print("Ты только что заработал 10 очков")

#упражнение 5-5
alien_color = 'red'
if alien_color == 'green':
    print("Ты только что заработал 5 очков")
elif alien_color == 'yellow':
    print("Ты только что заработал 10 очков")
elif alien_color == 'red':
    print("Ты только что заработал 15 очков")

#упражнение 5-6
year = 66
if year < 2:
    age = 'младенец'
elif year < 4:
    age = 'малыш'
elif year < 20:
    age = 'подросток'
elif year < 65:
    age = 'взрослый'
else:
    age = 'пожилой человек'
print(age)

#упражнение 5-7
i = 'peach'
favorite_fruits = ['apple', 'lemon', 'peach']
if i in favorite_fruits:
    print("You really like bananas")
elif i not in favorite_fruits:
    print("You really like orange")
