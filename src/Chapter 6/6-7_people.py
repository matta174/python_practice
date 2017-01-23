


person_0 = {
    'first name': 'luke',
    'last name': 'little',
    'age': '22',
    'city': 'buford'
}
person_1 = {
    'first name': 'matthew',
    'last name': 'compton',
    'age': '22',
    'city': 'dahlonega'
}
person_2 = {
    'first name': 'cody',
    'last name': 'stallings',
    'age': '22',
    'city': 'habersham'
}
people = [person_0,person_1,person_2]

for person in people:
    
   full_name = person['first name'] +' ' + person['last name']
   location = person['city']
   age = person['age']

   print('\n Name: '+full_name.title())
   print('\t Age: '+age)
   print('\t City: '+location.title())






