languages = ['english','german','french','spanish'] #Creates original list of languages

languages.append('russian') #appends or  adds to end of list
print(languages)

languages.insert(2,'swahili') #inserting at place 2 in list swahili
print(languages)

languages.remove('english') #removes data = english
print(languages)

print(languages.pop())#removes and returns last item in list
print(languages)

del languages[2] #delets language at second spot
print(languages)

languages.append('english') #adds back english
languages.append('mandarin') #adds mandarin
print(languages)

print(sorted(languages)) #temporarily sorts alphabetically

languages.reverse() #reverses order of languages
print(sorted(languages)) #temporarily alphabetically sorts again

languages.reverse() #reverses back to original
print(languages)

languages.sort() #perm sorts alphabetically
print(languages)

languages.sort(reverse=True) #reverses alphabetical sort
print(languages)



print('The list is now ' + str(len(languages)) +' languages long.')

