
name_magicians = ['xx', 'yy', 'ii']
make_magicians = []

def show_magician(name_magicians, make_magicians):
    while name_magicians:
        make_mgs = name_magicians.pop()
        
        print(make_mgs)
        make_magicians.append(make_mgs)
        
make_magicians_1 = []

def make_great(make_magicians):
    while make_magicians:
    
        make_magician = make_magicians.pop()
        make_magician = 'Great ' + make_magician
        make_magicians_1.append(make_magician)
        print("Hello, " + make_magician + "!")
        

show_magician(name_magicians[:], make_magicians)

make_great(make_magicians[:])



print(name_magicians)
print(make_magicians)
print(make_magicians_1)
