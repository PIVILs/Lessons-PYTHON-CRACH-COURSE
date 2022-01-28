
try:
    a = int(input('pleace first namber: '))
    b = int(input('pleace second namber: '))
    print(a/b)
except ValueError:
    print("You entered not a number.")
except ZeroDivisionError:
    print("You can't divide by zero!")
