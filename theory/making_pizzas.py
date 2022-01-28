#импортирование всего модуля
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushooms', 'green peppers', 'extra cheese')


#импортирование конкретных функций

from pizza import make_pizza

make_pizza(16, 'pepperoni') # при таком способе использовать точечную запись не обязательно
make_pizza(12, 'mushooms', 'green peppers', 'extra cheese')

#назначение псевдонима для функции
#make_pizza() назначается псевдоним mp()

from pizza import make_pizza as mp

mp(16, 'pepperoni') 
mp(12, 'mushooms', 'green peppers', 'extra cheese')

#назначение псевдонима для модуля

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushooms', 'green peppers', 'extra cheese')

#импортирование всех функций модуля

from pizza import*

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushooms', 'green peppers', 'extra cheese')
