FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

def convert_to_celsius(temperature):
    temparature_in_celsius = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temparature_in_celsius



def convert_to_fahrenheit(temperature):   
    temparature_in_fahrenheit = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temparature_in_fahrenheit

match unit:
    case "F":
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
    case "C":
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")

    case _:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
           

if __name__ == "__main__":        
    convert_to_celsius(temperature)
    convert_to_fahrenheit(temperature)
