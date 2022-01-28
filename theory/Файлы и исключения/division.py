# блок try-except

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#Использование исключений для предотвращения аварийного завершения программы

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_namber = input("\nFirst number: ")
    if first_namber == 'q':
        break
    second_namber = input("\nSecond number: ")
    if second_namber == 'q':
        break
    try:
        answer = int(first_namber)/int(second_namber)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
