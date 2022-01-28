def make_album(name, album_title, trek =' '):
    """Возвращает альбом с имене и названием, кол-во треков"""
    person = {'name': name, 'albom title': album_title}
    if trek:
        person['trek'] = trek
    return person
    
albums = make_album('ария', 'химера', trek=12)
print(albums)

albums = make_album('би-2', 'гранатовый браслет')
print(albums)



