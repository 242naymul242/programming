temperature_fahrenheit = int(input("Please type in a temperature (F): "))
degrees_celsius = (temperature_fahrenheit - 32) / 1.8000
print(f"{temperature_fahrenheit} degrees Fahrenheit equals {degrees_celsius} degrees Celsius")
if degrees_celsius < 0:
    print("Brr! It's cold in here!")