

cities = {
    'kansas city' : {
        'country':'usa',
        'population': 467007,
        'fact': 'Kansas City is actually in two states.'
    },

    'london': {
        'country': 'uk',
        'population': 8600000,
        'fact': 'London was founded by the Roman Empire.'
    },

    'paris': {
        'country': 'france',
        'population': 2150000,
        'fact':'Paris is the location of the Eiffel Tower.'
    }
}
for city, information in cities.items():
    print('\nCity: '+city.upper())
    information = 'Country: '+information['country'].upper()+'\nPopulation: '+str(information['population'])+'\nFun fact: '+information['fact']

    print(information)