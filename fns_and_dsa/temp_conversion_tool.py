FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = float(input("Enter the temperature to convert: "))
temp2 = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_celsius(temp):
    if temp2 == "F":
        in_celsius = (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f"{temp}°F is {in_celsius}°C")



def convert_to_fahrenheit(celsius):
    if temp2 == "C":
        in_fahrenheit = (temp * FAHRENHEIT_TO_CELSIUS_FACTOR) + 32
        print(f"{temp}°C is {in_fahrenheit}°F")

if __name__ == "__main__":        
    convert_to_celsius(temp)
    convert_to_fahrenheit(temp)
