print("Welcome to the Fahrenheit/Celsius converter!")


def main():
    while True:
        global Temp
        Temp = input("Will you be converting to F or to C?: ").lower()
        if Temp == "f":
            celsius = int(input("Enter your temperature in Celsius: "))
            F = (celsius * (9 / 5) + 32)
            new_fahrenheit = "{0:.1f}".format(F)
            print('{}C is {}F'.format(celsius, new_fahrenheit))
        elif Temp == "c":
            fahrenheit = int(input("Enter your temperature in Fahrenheit: "))
            C = ((fahrenheit - 32) * (5 / 9))
            new_celsius = "{0:.1f}".format(C)
            print('{}F is {}C'.format(fahrenheit, new_celsius))
        else:
            Temp = input("Please enter 'F' or 'C': ").lower()


if __name__ == '__main__':
    main()