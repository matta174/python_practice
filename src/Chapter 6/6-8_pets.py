burt = {
    'name': 'burt',
    'owner': 'matthew',
    'type': 'dog'
}
tux = {
    'name': 'tux',
    'owner': 'susan',
    'type': 'cat'

}
fuzzbut = {
    'name': 'fuzzbut',
    'owner': 'susan',
    'type': 'cat'
}
pets = [burt,tux,fuzzbut]

for pet in pets:
    name = pet['name']
    owner = pet['owner']
    type = pet['type']

    print('\n Name: ' + name.title())
    print('\t Owner: '+owner.title())
    print('\t Type: '+type.title())