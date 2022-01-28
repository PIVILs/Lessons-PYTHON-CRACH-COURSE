
#метод replace() замена любого слова в строке другим словом

with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents.replace('Python', 'C').rstrip())
