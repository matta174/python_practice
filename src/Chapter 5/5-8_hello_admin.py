#Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log
#in to a website. Loop through the list and print a greeting to each user

users = ['matthew','cody','josh','jasmine','admin']

for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print("Hello "+user.title()+", thank you for logging in again.")