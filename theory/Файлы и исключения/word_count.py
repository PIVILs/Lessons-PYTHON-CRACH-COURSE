#Работа с несколькими файлами

def count_words(filename):
    """Подсчет приблизительного колличества слов в файле"""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Подсчет приблизительного колличества слов в файле
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + 
            " words.")
        
filename = 'alice.txt'
count_words(filename)

#работа с несколькими файлами

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


#pass команда с которой блок ничего не делает

def count_words(filename):
    """Подсчет приблизительного колличества слов в файле"""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Подсчет приблизительного колличества слов в файле
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + 
            " words.")
        
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
