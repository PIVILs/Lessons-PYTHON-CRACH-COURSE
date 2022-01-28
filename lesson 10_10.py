
def count_given_words(filename):
    """Подсчет приблизительного колличества слов в файле"""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Подсчет приблизительного колличества слов 'The' в файле
        words = contents.lower().count('the')
        print('Count given words: ' + str(words))
        
filenames = ['The Genetic Effects of Radiation.txt', 'siddhartha.txt']
for filename in filenames:
    count_given_words(filename)
