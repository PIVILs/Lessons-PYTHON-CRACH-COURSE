#if со списками
#проверка специальных значений
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
         print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

#проверка наличия элементов в списке
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#множественные списки
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
                      'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
        
print("\nFinished making your pizza!")

#упражнения 5-8
names = ['admin', 'JOHN', 'Fred', 'richard', 'Donald']
for name in names:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + name + ", thank you for logging in again!")


#упражнение 5-9
names = []
if names:
    for name in names:
        print("Хоть ктот из пользователей")
else:
        print('We need to find some users!')

#упражнение 5-10
current_users = ['admin', 'JOHN', 'oVec', 'richard', 'Donald']
new_users = ['admin', 'john', 'Ovec', 'Rick', "Donald's"]
current_users_lower = {i.lower() for i in current_users} #проверка имен в строчном регистре
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('имя занято, выбери другое')
    else:
        print('Hello ' + new_user + '!')
print(current_users)
print(new_users)
    
#упражнение 5-11
# порядковые числительные в английском заканчиваются суффиксом th, кроме 1st, 2nd, 3rd
numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
print(numbers)
for number in numbers:
    if number == '1':
        print(number+'st')
    elif number == '2':
        print(number+'nd')
    elif number == '3':
        print(number+'rd')
    else:
        print(number+'ht')

 
#упражнение 5-12
#мои идеи по решению задач:
#в первую очередь это решение задач из проекта Эйлера. Я их начну решать кода изучу по книге все главы из части 1
#идея разработать свое веб приложение или сайт на Джанго или спомощь какого другого фреймворка
#потренероватьря в решении задач на других языках: Java, C++, C#, HTML, SQL, Ruby
#изучить все лекции и практические задания по PHYTHON из МФТИ от Тимофея Хирьянова
