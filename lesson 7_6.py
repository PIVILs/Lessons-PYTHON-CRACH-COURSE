f = True
while f:
    age = input("\nindicate age: ")
    if age.isdigit() == False or int(age) < 0:     #проверка на цифры или буквы
        age = input("\nВведите возраст цифрами: ")
        
    else:
        f = False
          
    
        while True:
            
            age = int(age)    
            if age >= 13:
                i = 15
                print("\nPrice " + str(i) + "$")
        
            elif age <= 3:
                i = 0
                print("\nPrice " + str(i) + "$")
            else:
                i = 10
                print("\nPrice " + str(i) + "$")
            break
    
    f = True

