unit = input("Is this temperature in Celsius or Fahrgenheit (C or F): ").lower()
temp = float(input("What is the temperature:"))
if unit == "c":
    conveted = temp *9/5 + 32
    print(f"{temp} degrees Celsius is {conveted} degrees Fahrenheit")
elif unit == "f":
    convert = (temp - 32) * 5/9
    print(f"{temp} degrees Fahrenheit is {convert} degrees Celsius")
else:
    print(f"{unit} is not a valid unit...👶🏻")