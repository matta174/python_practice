
locations = {}

polling_status = True

while polling_status:
    name = input('Type your name.\n')
    responce = input('Where is your dream vacation?\n')

    locations[name]= responce

    repeat = input('Would you like for someone else to take the poll?\n')
    if repeat == 'no':
        polling_status = False

print('--- Poll Results ---\n')
for name, location in locations.items():
    print(name +' would like to go to '+ location + ' for vacation.\n')