famous_guest_list = ['napoleon bonaparte','george orwell','alexander the great']
print("Oh no! it turns out "+famous_guest_list[0].title() + " won't be able to make it!\n")
famous_guest_list[0] = 'ronald reagan'
print('Hey everyone, luckily I was able to find a larger table to accomodate more people!\n')
famous_guest_list.insert(0,'franklin delano roosevelt')
famous_guest_list.insert(2,'john f kennedy')
famous_guest_list.append('thomas jefferson')
print("Unfortunately that table won't be able to arrive in time. Instead I only have space for two guests")



persontoleave = famous_guest_list.pop()
print('Sorry '+persontoleave.title()+" there just wasn't enough room for you. \n")
persontoleave = famous_guest_list.pop()
print('Sorry '+persontoleave.title()+" there just wasn't enough room for you. \n")
persontoleave = famous_guest_list.pop()
persontoleave = famous_guest_list.pop()
print('Sorry '+persontoleave.title()+" there just wasn't enough room for you. \n")

print("I'm happy to say that you "+famous_guest_list[0].title()+" are still invited!\n")
print("I'm happy to say that you "+famous_guest_list[1].title()+" are still invited!\n")

del famous_guest_list[0]
del famous_guest_list[0]
print(famous_guest_list)
