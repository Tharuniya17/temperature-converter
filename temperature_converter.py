def convert_temperature(value, from_unit):
    from_unit = from_unit.lower()

    if from_unit == "celsius":
        celsius = value
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15

    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5/9
        fahrenheit = value
        kelvin = celsius + 273.15

    elif from_unit == "kelvin":
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        kelvin = value

    else:
        print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")
        return

    print(f"\n✅ Converted Temperatures:")
    print(f"🌡 Celsius: {celsius:.2f} °C")
    print(f"🌡 Fahrenheit: {fahrenheit:.2f} °F")
    print(f"🌡 Kelvin: {kelvin:.2f} K")

# Main Program
print("🔁 Temperature Converter")
print("------------------------")
try:
    temp_value = float(input("Enter the temperature value: "))
    temp_unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ")
    convert_temperature(temp_value, temp_unit)
except ValueError:
    print("⚠ Please enter a valid number for temperature.")