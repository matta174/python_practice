#This program is meant to check to see if the data in a message contains a phone number and returns true or false.

def is_phone_number (text):
    if len(text) != 12:
        return False
    for i in range (0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range (4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


print('770-317-1552 is a phone number:')
print(is_phone_number('770-317-1552'))

print('Moshi Moshi is a phone number:')
print(is_phone_number('Moshi Moshi'))