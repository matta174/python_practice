sandwich_orders =['Tuna','Turkey','Club','Cuban']

finished_orders =[]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made your ' + current_sandwich + ' sandwich')
    finished_orders.append(current_sandwich)

print('Each sandwich has been made')
print(sandwich_orders)
print(finished_orders)