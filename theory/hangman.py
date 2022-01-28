import random
HANGMAN_PICS =['''
    +---+
        |
        |
        |
       ===''','''
    +---+
        |
        |
        |
       ===''','''
    +---+
    0   |
    |   |
        |
       ===''','''
    +---+
    0   |
   /|   |
        |
       ===''','''
    +---+
    0   |
   /|\  |
        |
       ===''','''
    +---+
    0   |
   /|\  |
   /    |
       ===''','''
    +---+
    0   |
   /|\  |
   / \  |
       ===''']
words ='аист акула бабуин баран барсук  бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея
индюк кит кобра коза козел койот корова кошкакролик крыса курица лама ласка лебедь лев лиса лосось лось ля- 
гушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон
попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек чрепаха ястреб ящерица'.split()

def getRandomWord(wordList):
    # Эта функция возврвщает случайную строку из переданного списка
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HAGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные  буквы'), end=' ')
    for letter in missedLetter:
        print()

        blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):# заменяет пропуски отгаданнами буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[i:] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Показывает секретное слово с пробелами между буквами
        print(letter, end=' ')
    print()
    
def getGuess(alreadyGuessed):
    #Возвращает букву, введенную игроком.Эта функция проверяет, что игрок ввел только одну букву и ничего больше.
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.Lower()
        if len(guess) != 1:
            print('Пожалуйста введите еще одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже назвали эту букву.Назовите другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите Букву.')
        else:
            return guess

def playAgain():
    #Эта функция возвращает значение True,если игрок хочет сыграть заново;в противном случае возвращает False.
    print('Хотите сыграть еще?(да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')
missed letters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gamelsDone = False

while True:
    displayBoard(missedLetters + correctLetters)
