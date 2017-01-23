favorite_numbers = {
    'cody':[2,4],
    'jasmine':[9],
    'matthew':[33],
    'josh':[7],
    'chase':[68,42,14],
    'garrett':[11,22]
}

for name, numbers in favorite_numbers.items():
    print('\n'+name.title()+"'s favorite numbers are: ")
    for numbers in numbers:
        print(str(numbers))