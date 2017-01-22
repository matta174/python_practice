
ordinal_numbers = [1,2,3,4,5,6,7,8,9]

for place in ordinal_numbers:
    if place == 1:
        print(str(place) +'st')
    elif place == 2:
        print(str(place)+'nd')
    elif place == 3:
        print(str(place)+'rd')
    else:
        print(str(place)+'th')


print()