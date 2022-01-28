
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


#создание пустого списка для хранения пришельцев
aliens = []
#создание 30 зеленых пришельцев
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#превратить первых 3-х в желтых
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':#и в красных
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


#вывод первых 5 пришельцев.
for alien in aliens[:5]:
    print(alien)
print('...')

#вывод количества созданных пришельцев.
print("Total number of aliens: " + str(len(aliens)))
