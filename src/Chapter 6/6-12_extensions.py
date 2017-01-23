rivers = {
    'nile': {
        'country':'egypt',
        'length': '4,258 miles long'
    },
    'amazon':{
        'country':'brazil',
        'length' : '4,345 miles long'
    },

    'mississippi':{
        'country':'usa',
        'length' : '2,320 miles long'
    }
}
for river, information in rivers.items():
    print('\nRiver: '+ river.title())
    information ='Country: ' + information['country'].upper() + '\nRiver length: ' + information['length']
    print(information)
