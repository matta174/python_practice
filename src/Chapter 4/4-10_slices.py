pizzas = ['pepperoni','cheese','sausage','pineapple','bacon','meat lovers','vegetarian','marinara','white','hawaiian']
print('The first three items in the list are: ' )
for pizza in pizzas[:3]:
    print(pizza.title())

print('Three items from the middle of the list are: ')
for pizza in pizzas[3:6]:
    print(pizza.title())

print('The last three items from the list are: ')
for pizza in pizzas[7:11]:
    print(pizza.title())