def make_sandwich(*toppings):
    """Выводит описание сэндвича."""
    print("\nMaking a sandwich with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
        
make_sandwich('pepperoni')
make_sandwich('mushooms', 'green peppers', 'extra cheese')

