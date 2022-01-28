
from random import randint

#x = randint(1,6)

#print(str(x))

class Die():
    
    def __init__(self, sides):
        
        self.sides = sides
    
    def roll_die(self):
        self.sides = randint(1,6)

        print('\n' + str(self.sides))
        

 
y = Die('6')
y.roll_die()



def again():
    a = '\nplease again? (y/n)  '
        
    while True:
        b = input(a)
        if b == 'y':
            y.roll_die()
            
        else:
            print('\nBye')
            False

again()
