


prompt = 'Type something and see me parrot it back to you, I will only do it four times though. \n'
prompt += 'You can also type "quit" if you want to leave'

active = True
count = 0
while active:
    message = input(prompt + '')

    if message != 'quit':
        print(message)
        count += 1
    if count >= 4:
        active = False
    if message == 'quit':
        break

