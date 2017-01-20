my_pizzas = ['pepperoni','cheese','sausage']
friend_pizzas = ['pepperoni','cheese','sausage']

my_pizzas.append('hawaiian')
friend_pizzas.append('bacon')

print('My favorite pizzas are: ')
for pizza in my_pizzas:
    print(pizza.title())

print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza.title())