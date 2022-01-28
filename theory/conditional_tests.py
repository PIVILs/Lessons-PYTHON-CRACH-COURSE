#упражнение 5-2
digits = ['0','1','2','3','4','5','6','7','8','9']
for digit in digits:
    if digit == '5':
        print(True)
    else:
        print(False)


for digit_5 in digits:
    if digit_5 != '5':
        print(True)
    else:
        print(False)

for digit_5 in digits:
    if digit_5 >= '5':
        print(True)
    else:
        print(False)

for digit_5 in digits:
    if digit_5 <= '5':
        print(True)
    else:
        print(False)

i = '4'

if i not in digits:
    print(i.title()+ ", not listed.")

if i in digits:
    print(i.title()+ ", is on the list.")
