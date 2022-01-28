number = input("Проверь, кратно ли 10 твое число: ")
number = int(number)

if number %10 == 0:
    print("\nДа, число " + str(number) + " кратно 10")
else:
    print("\nНет, число " + str(number) + " не кратно 10.")
    

