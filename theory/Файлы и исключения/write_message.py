
#Запись в файл

#Запись в пустой файл

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    
    
# w - запись
# r - чтение
# a - присоединение
# r+  - как чтение так и запись

#присоединение данных к файлу

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large detasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
