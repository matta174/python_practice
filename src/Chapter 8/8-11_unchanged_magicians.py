

magicians = ['bill', 'bob', 'george']


def show_magicians(list):
    for magician in magicians:
        print(magician.title() + " Hello!")


def make_great(list):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + " the Great!"
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians = ['bill', 'bob', 'george']
show_magicians(magicians)
print('\n')

great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print('\n')
show_magicians(magicians)
