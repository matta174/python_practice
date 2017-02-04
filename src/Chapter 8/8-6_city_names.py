


def city_country(city,country):
    print(city.title() + ', ' + country.title())
while True:
    city = input('Please provide a city\n')
    if city == 'q':
        break
    country = input('Please provide a country\n')
    if country == 'q':
        break
    city_country(city,country)

