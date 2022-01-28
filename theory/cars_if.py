#команды if
cars = ['audi', 'bmw', 'subaru', 'toyota']
print(cars)
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#!= отрицание. грибы(mushrooms), запрошенный топпинг(requested_topping)
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')

#сравнение чисел answer(ответ)
answer = 17
if answer != 42:
    print("That is not the corrent answer. Please try again!")

#проверка вхождения значения в список
requested_topping = ['mushrooms', 'onions', 'pineapple']
for mushrooms in requested_topping:
    print('True')
for pepperoni in requested_topping:
    print('False')

#not ключевое слово, для проверки того, что значение не входит в список
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title()+ ", you can post a response if you wish.")

#логические выражения True или False

#упражнения 5-1
car = 'lada'
print("Is car == 'lada'? I predict True.")
print(car == 'lada')
print("\nIs car == 'volga'? I predict False")
print(car == 'volga')
print("\nIs car == 'volga' or 'lada'? I predict False")
print(car == 'volga' or 'lada')
print("\nIs car == 'volga' and 'lada'? I predict False")
print(car == 'volga' and 'lada')
