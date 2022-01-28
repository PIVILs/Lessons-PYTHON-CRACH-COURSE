

def make_album(name, album_title,):
    """Возвращает альбом с именем и названием"""
    person = {'name': name, 'albom title': album_title}
    return person
    
while True:
    print("\nВведите исполнителя и название альбома: ")
    print("(enter 'q' at any time to quit) ")
    
    name = input("\nИсполнитель: ")
    if name == 'q':
        break
        
    album_title = input("\nНазвание альбома: ")
    if album_title == 'q':
        break

    albums = make_album(name, album_title)
    print(albums)
