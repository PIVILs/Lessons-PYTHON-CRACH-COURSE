
answers = 'answers.txt'

while answers:
    answer = input('Почему тебе нравиться программировать?\n\n')
    with open(answers, 'a') as file_object:
        file_object.write(answer + '\n')
