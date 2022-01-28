def count_words(filename):

    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
            print(contents)
    except FileNotFoundError:
        print('нет одного из файлов')
        pass
    
        
filenames = ['cats.txt', 'dogs.txt', 'siddhartha.txt']
for filename in filenames:
    count_words(filename)
