
message = input("Tell me someyhing, and I will repeat it back to you: ")
print(message)

prompt = "\nTell me someyhing, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
