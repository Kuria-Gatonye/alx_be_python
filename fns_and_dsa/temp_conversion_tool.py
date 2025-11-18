#global variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#functions
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius  * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

#User input
temp = int(input("Enter the temperature to convert: "))
if not temp.is_integer():
    print("Invalid temperature. Please enter a numeric value.")
else:
    mode = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if mode == "C":
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")
        
    elif mode == "F":
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted}°C")

    else:
        print("No mode was specified")

    