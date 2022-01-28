sandwich_orders = ['black', 'chikenburger', 'bigmak']
finished_sandwiches = []


while sandwich_orders:
    sandwich = sandwich_orders.pop()
    
    print("I made your tuna sandwich: " + sandwich.title())
    finished_sandwiches.append(sandwich)
    

print("\nИзготовлены следующие сендвичи: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

