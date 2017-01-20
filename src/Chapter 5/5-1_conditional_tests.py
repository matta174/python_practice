#Evaulating conditional tests

transports = ['train','automobile','horseback','plane','boat']

print("Is sleep a mode of travel? ")
if 'sleep' in transports:
    print("True\n")
elif 'sleep' not in transports:
    print("False\n")

age = 22
print('Am I 22? I bet so..')
print(age == 22)

friends_age = 12
print('Is my friend 22? I doubt it.')
print(friends_age == 22)

print('Am I 22 and my friend 12? I bet so..')
if age == 22 and friends_age == 12:
    print(True)
else:
    print(False)

print(age > 21)
print(age < 21)
print(friends_age >21 and age<=23)

print(age >= 21 and 'train' in transports)

print('sleep' in transports or 'automobile' in transports)

travel = 'foot'

if travel in transports:
    print('Acceptable mode of transportation')
else:
    print('Not an acceptable mode of transportation')
