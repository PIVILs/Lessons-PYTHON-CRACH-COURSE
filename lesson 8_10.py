
name_magicians = ['xx', 'yy', 'ii']
make_magicians = []

def show_magician(name_magicians, make_magicians):
    while name_magicians:
        make_mgs = name_magicians.pop()
        
        print(make_mgs)
        make_magicians.append(make_mgs)

def make_great(make_magicians):
    
    for make_magician in make_magicians:
        make_magician = 'Great ' + make_magician
        print("Hello, " + make_magician + "!")

show_magician(name_magicians, make_magicians)
make_great(make_magicians)

print(make_magicians)
