
#Работа с содержимым файла

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))


#Большие файлы: миллион цифр

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string[:52] + "...")
print(len(pi_string))


#Проверка дня рождения

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input("Enter your birthday, in the form ddmmyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
