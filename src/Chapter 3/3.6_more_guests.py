famous_guest_list = ['napoleon bonaparte','george orwell','alexander the great']

message= "Hello "+famous_guest_list[0].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[1].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[2].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)

print("Oh no! it turns out "+famous_guest_list[0].title() + " won't be able to make it!\n")
famous_guest_list[0] = 'ronald reagan'

message= "Hello "+famous_guest_list[0].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[1].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[2].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)

print('Hey everyone, luckily I was able to find a larger table to accomodate more people!\n')
famous_guest_list.insert(0,'franklin delano roosevelt')
famous_guest_list.insert(2,'john f kennedy')
famous_guest_list.append('thomas jefferson')

message= "Hello "+famous_guest_list[0].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[1].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[2].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[3].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[4].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[5].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)