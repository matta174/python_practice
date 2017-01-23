
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
people_to_take_poll = ['jen','sarah','matthew','cody','chase','phil']

for person in people_to_take_poll:
    if person not in favorite_languages.keys():
        print(person.title()+ ' you need to take the poll.\n')
    else:
        print('Thanks '+person.title()+' for taking the poll.\n')


