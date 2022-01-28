#Изменение списка в функции

#Список моделей, которые необходимо напечатать.
unprinted_desings = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#цикл последовательно печатает каждую модель до конца списка.
# После печати модель перемещается в список completed_models.
while unprinted_desings:
    current_desing = unprinted_desings.pop()
    #Печать модели на 3в-принтере
    print("Printing model: " + current_desing)
    completed_models.append(current_desing)

#вывод всех готовых моделей.
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)


#две функции

def print_models(unprinted_desings, completed_models):
    """
    Имитирует печать моделей, пока список не станет пустым
    каждая модель после печати перемещается в completed_models
    """
    while unprinted_desings:
        current_desing = unprinted_desings.pop()
        
        #Имитация печати
        print("Printing model: " + current_desing)
        completed_models.append(current_desing)
        
def show_completed_models(completed_models):
    """выводит информацию обо всех напечатанных моделях."""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_desings = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_desings, completed_models)
show_completed_models(completed_models)
