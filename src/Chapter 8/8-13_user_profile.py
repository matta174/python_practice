def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return  profile

user_profile = build_profile('Matthew','Compton',location = 'Dahlonega', field= 'Computer Science',learning_python = True)
print(user_profile)