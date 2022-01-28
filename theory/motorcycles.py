motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles.insert(0,'восход')
print(motorcycles)

del motorcycles[-1]
print(motorcycles)

#pop метод удаляет последний элемент из списка, но позволяет работать с ним после удаления
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nА " + too_expensive.title()+ " слишком дороговат для меня.")
