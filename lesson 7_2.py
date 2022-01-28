number_of_places = input("На какое колличество мест? ")
number_of_places = int(number_of_places)

if number_of_places >8:
    print("\nУвы, придеться подождать")
else:
    print("\nЗабронировано под Вас " + str(number_of_places) + " места")
    

