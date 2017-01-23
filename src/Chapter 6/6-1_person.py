#Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city.

person = {
    'first name': 'luke',
    'last name': 'little',
    'age': '22',
    'city': 'buford'
}
print(person['first name'].title() +
      ' '+
      person['last name'].title() +
      ' is '+
      str(person['age'])+
      ' years old and lives in '+
      person['city'].title()
      )