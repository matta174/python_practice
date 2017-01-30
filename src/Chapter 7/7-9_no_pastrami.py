sandwich_orders =['Tuna','pastrami','Turkey','Club','Cuban','pastrami','roast beef','pastrami']


print('Unfortunately we are all out of pastrami folks.\n')

while 'pastrami' in sandwich_orders:
 print(sandwich_orders)
 sandwich_orders.remove('pastrami')

finished_orders =[]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made your ' + current_sandwich.title() + ' sandwich\n')
    finished_orders.append(current_sandwich)

print('Each sandwich has been made')