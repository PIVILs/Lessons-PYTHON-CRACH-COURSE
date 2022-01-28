prompt = "\nindicate age: "

while True:
    age = input(prompt)
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
