sandwich_orders = ['pastrami', 'black', 'chikenburger', 'pastrami', 'bigmak', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    
    print("I made your tuna sandwich: " + sandwich.title())
    finished_sandwiches.append(sandwich)
    

print("\nИзготовлены следующие сендвичи: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())


