

prompt = 'Enter your age to see the price of your movie ticket. '

while True:
    age = int(input(prompt + ' '))

    if age < 3:
        print('Your ticket is free! ')
        break
    if age < 12:
        print('Your ticket is $10 ')
        break
    if age > 12:
        print('Your ticket is $15 ')
        break