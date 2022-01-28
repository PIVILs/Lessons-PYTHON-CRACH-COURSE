guest = ['Ленин', 'Троцкий', 'Черчиль', 'Александр Первый']
print(guest[0].title())
print(guest[1].title())
print(guest[-2].title())
print(guest[-1].title())

invitation = "\n\t Invite to dinner " + guest[0].title()+"."
print(invitation)
invitation = "\n\t Invite to dinner " + guest[1].title()+"."
print(invitation)
invitation = "\n\t Invite to dinner " + guest[2].title()+"."
print(invitation)
invitation = "\n\t Invite to dinner " + guest[-1].title()+"."
print(invitation)


will_not_come = guest.pop(2)
print("\nUnfortunately " + will_not_come + " will not com!")

guest.insert(2, "Сталин")


invitation = "\n\t Invite to dinner " + guest[0].title()+"."
print(invitation)
invitation = "\n\t Invite to dinner " + guest[1].title()+"."
print(invitation)
invitation = "\n\t Invite to dinner " + guest[2].title()+"."
print(invitation)
invitation = "\n\t Invite to dinner " + guest[-1].title()+"."
print(invitation)

#Расширение списка гостей!

print(guest)

guest.insert(0, "Петр Первый")
guest.insert(2, "Екатерина Вторая")
guest.append("Горбачев")

invitation = "\n\t Invite to dinner " + guest[0].title()+"."
print(invitation)
invitation = "\n\t Invite to dinner " + guest[1].title()+"."
print(invitation)
invitation = "\n\t Invite to dinner " + guest[2].title()+"."
print(invitation)
invitation = "\n\t Invite to dinner " + guest[3].title()+"."
print(invitation)
invitation = "\n\t Invite to dinner " + guest[-3].title()+"."
print(invitation)
invitation = "\n\t Invite to dinner " + guest[-2].title()+"."
print(invitation)
invitation = "\n\t Invite to dinner " + guest[-1].title()+"."
print(invitation)

print(guest)

#Уменьшение списка гостей!

will_not_come = guest.pop(-1)
print("\nК сожалению, на тебя милый " + will_not_come + " не хватит мест!")
will_not_come = guest.pop(-1)
print("\nК сожалению, на тебя милый " + will_not_come + " не хватит мест!")
will_not_come = guest.pop(-1)
print("\nК сожалению, на тебя милый " + will_not_come + " не хватит мест!")
will_not_come = guest.pop(-1)
print("\nК сожалению, на тебя милый " + will_not_come + " не хватит мест!")
will_not_come = guest.pop(-1)
print("\nК сожалению, на тебя милый " + will_not_come + " не хватит мест!")

print(guest)

invitation = "\n\t Invite to dinner " + guest[0].title()+"."
print(invitation)
invitation = "\n\t Invite to dinner " + guest[1].title()+"."
print(invitation)

del guest[1]
del guest[0]
print(guest)
print(len(guest)) #функция len() определяет длину списка

