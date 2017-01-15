motorcycles = ['BMW','Honda','Harley Davidson','Ducati']
print(motorcycles)
message = "My favorite motorcycle is a "+motorcycles[0]
print(message)

print("I would like to own a "+motorcycles[1]+ " motorcycle.\n")

motorcycles.append('Yamaha')
print(motorcycles )

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[2]
print(motorcycles)

motorcycles = ['yamaha','honda','harley davidson','ducati']
last_motorcycle = motorcycles.pop()

print(motorcycles)
print("The last motorcycle I owned was a "+last_motorcycle.title())

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a '+ first_owned.title())
