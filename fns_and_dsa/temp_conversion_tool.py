# Global variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# function convert_to_celsius(fahrenheit) that takes a temperature in Fahrenheit
#  and returns the temperature converted to Celsius.
def convert_to_celsius(fahrenheit: float):

    celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius

def convert_to_fahrenheit(celsius: float):
    temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temp

user_temperature = input("Enter the temperature to convert: ")
if user_temperature.isdecimal() == True:
    user_temperature = float(user_temperature)

    temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if temp_type == 'C':
        conversion = convert_to_fahrenheit(user_temperature)
        print(f"{user_temperature}°C is {conversion}°F")

    elif temp_type == 'F':
        conversion = convert_to_celsius(user_temperature)
        print(f"{user_temperature}°F is {conversion}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")




