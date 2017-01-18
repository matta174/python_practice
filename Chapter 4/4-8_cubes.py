#Make a list of the first 10 cubes and use a for loop to print out the value of each cube
numbers = []
for number in range(1,11):
    numbers.append(number **3)
    print(number**3)
print(numbers)