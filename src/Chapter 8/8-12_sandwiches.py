def make_sandwich(*items):
    print("I'm going to make you a sandwich with:")
    for topping in items:
        print(topping.title())
    print('Finished!')


make_sandwich('turkey','balogna','mustard')

print('\n')

make_sandwich('ham','cheese')

print('\n')

make_sandwich('tuna','asparagus','turkey')