class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Returns a nice description of name and cuisine type."""
        description = self.restaurant_name + " is a " + self.cuisine_type.title() + " restaurant. \n"
        return description

    def open_restaurant(self):

        message = self.restaurant_name + ' is now open for business! \n'
        return message


my_new_restaurant = Restaurant("Cugino's",'italian')
print(my_new_restaurant.describe_restaurant())


pizza = Restaurant('Papa Johns','Pizza')
print(pizza.describe_restaurant())

slammin_sams = Restaurant('Slammin Sams','french')
print(slammin_sams.describe_restaurant())
