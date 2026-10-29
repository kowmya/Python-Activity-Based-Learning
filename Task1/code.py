
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")

if celsius >= 40:
    print("Warning: Extreme Heatwave Conditions!")
elif celsius >= 30:
    print("Weather is Hot and Sunny.")
else:
    print("Weather is pleasant.")
