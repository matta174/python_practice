
favorite_places = {
    'jasmine' : ['barcelona','seattle','alaska'],
    'matthew' : ['austria','kansas city','pamplona'],
    'kinsley' : ['ecuador','panama'],
    'susan' : ['croatia','prague','peru','ecuador']
}

for name, places in favorite_places.items():
    print('\n'+name.title() + "'s favorite places are: ")
    for places in places:
        print('\t' + places.title())