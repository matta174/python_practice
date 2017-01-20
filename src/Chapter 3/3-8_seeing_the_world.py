places_i_want_to_visit = ['taj mahal','the equator','moscow','australia','los angeles'] #declares the list initially
print(places_i_want_to_visit) #prints the data as is

print(sorted(places_i_want_to_visit)) #temporarily sorts the data in the list alphabetically, leaving original data

print(places_i_want_to_visit) #shows that the original list still exists

places_i_want_to_visit.reverse() #reverses the order of the list
print(places_i_want_to_visit) #prints reversed list

places_i_want_to_visit.reverse() #reverses again reverting it back to original list
print(places_i_want_to_visit) #prints newly returned original list

places_i_want_to_visit.sort() #permanently sorts list alphabetically
print(places_i_want_to_visit) #prints new list

places_i_want_to_visit.sort(reverse=True) #permanently reverses list alphabetically
print(places_i_want_to_visit) #prints new list