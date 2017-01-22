

current_users = ['matthew','cody','josh','Jasmine','admin']
new_users = ['matthew','corey','adriana','logan','jasmine']

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print('Sorry '+ user.title()+ ' that username is already taken.')
    else:
        print('Username available.')
