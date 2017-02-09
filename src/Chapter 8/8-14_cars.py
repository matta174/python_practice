def make_car(make,model,**user_info):
    car_dict = {
        'make' : make.title(),
        'model' :  model.title()
                }
    for info, value in user_info.items():
        car_dict[info] = value

    return car_dict

miata = make_car('Mazda','Miata',year = 94,miles = 150000)
print(miata)