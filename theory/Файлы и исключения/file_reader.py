
#Чтение всего файла

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#read()  метод который читает все содержимое файла
#rstrip вызов удаляет все пропуски в конце строки


#Пути к файлам

#with open('text_files\имя_файла.txt') as file_object:   относительный путь вызова

#file_path = 'C:\Users\ehmatthes\other_files\text_files\имя_файла.txt'
#with open(file_path) as file_object: абсолютный путь через переменную


#Чтение по строкам

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


#Создание списка строк по содержимому файла

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())        

#метод readlines() последовательно читает каждую строку из файла и сохраняет ее в список
