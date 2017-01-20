message = "Hello World!"

print('hello world'== message)
print('Hallo Welt!' == message)
print('hello world'== message.lower())

print(5 >6)
print(5>=5)
print(6<7)
print(5 == 2+3)
print(5 == 3+3)

if 5 == 1+4 and 5 >4 or 5==2+2:
    print(True)
else:
    print(False)


if 5 == 1+4 and 3>4 or 5==2+2:
    print(True)
else:
    print(False)

my_list = ['apple','tangerine','onion']

if 'apple' in my_list:
    print('Apple was in my list.')
else:
    print('That was not in my list')

if 'carrot' not in my_list:
    my_list.append('carrot')
    print('carrot has been added')
    print(my_list)

else:
    "That is already in my list"