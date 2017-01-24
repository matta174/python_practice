prompt = input('Give me a number and I will tell you if it is a multiple of ten')
number = int(prompt)

if number % 10 == 0:
    print(str(number)+' is a multiple of 10.')
else:
    print(str(number)+' is not a multiple of 10.')