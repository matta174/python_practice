class User ():
    def __init__(self,first_name,last_name,age,hair_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hair_color = hair_color

    def describe (self):
        message = self.first_name.title() + ' ' + self.last_name.title() + ' is ' + str(self.age) + ' years old and has ' + self.hair_color + ' hair.'
        return message

    def greet_user (self):
        message = 'Hello ' + self.first_name.title() +'!\n'
        return message


me = User('matthew','compton','22','brown')
print(me.describe())
print(me.greet_user())

cody = User ('cody','stallings','22','brown')
print(cody.describe())
print(cody.greet_user())

kinsley = User('kinsley','compton','27','blonde')
print(kinsley.describe())
print(kinsley.greet_user())