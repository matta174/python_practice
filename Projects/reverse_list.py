prompt = 'Please input whatever you would like. I will repeat it back to you backwards\n'
prompt += 'You can also type "quit" if you want to leave'

active = True
count = 0
list = []


while active:
    message = input(prompt + '\n')

    if message != 'quit':
        list.append(message)
    if message == 'quit':
        break

for i in reversed(list):
    print(i + '\n')