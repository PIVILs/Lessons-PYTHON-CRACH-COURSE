
guest = 'guest_book.txt'

while guest:
    name = input('name?\n\n')
    with open(guest, 'a') as file_object:
        file_object.write(name + '\n')
