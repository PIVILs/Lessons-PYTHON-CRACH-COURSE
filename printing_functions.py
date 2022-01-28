
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
