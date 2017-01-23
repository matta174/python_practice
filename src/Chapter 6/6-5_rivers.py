#Make a dictionary containing three major rivers and the country each river runs through.
rivers = {
    'nile':'egypt',
    'amazon':'brazil',
    'mississippi':'usa'
}

for river, country in rivers.items():
    if country == 'usa':
        print('The ' + river.title() + ' runs through ' + country.upper() + '.\n')
    else:
        print('The '+river.title()+' runs through '+country.title()+'.\n')

for river in rivers.keys():
    print(river.title())
print('\n')

for country in rivers.values():
    print(country.title())