#This program is meant to check to see if the data in a message contains a phone number and returns true or false.

def is_phone_number (text): #accepts text as input
    if len(text) != 12: #12 is length of normal North American phone number
        return False
    for i in range (0,3): #makes sure first three digits are numbers
        if not text[i].isdecimal():
            return False
    if text[3] != '-': #makes sure that third spot is a dash
        return False
    for i in range (4,7): #makes sure 4-7 digits are numbers
        if not text[i].isdecimal():
            return False
    if text[7] != '-': #makes sure spot at 7 is -
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


print('770-317-1552 is a phone number:')
print(is_phone_number('770-317-5555'))

print('Matthew Compton is really awesome. is a phone number:')
print(is_phone_number('Matthew Compton is really awesome.'))

message = 'You can reach me at 770-317-5555 anytime to hire me. 321-314-5555 is my house' #this little function checks through a whole message to see if it can find a number inside
for i in range (len(message)):
        chunk = message[i:i+12]
        if is_phone_number(chunk):
            print('Phone number found: ' + chunk)
print('Done')

