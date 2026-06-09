weight = float(input("Enter the weight: "))
unit = input("Enter the unit (kg, pounds): ").lower()
if unit == "kg":
    covert_in_pounds = weight * 2.20462
    print(f"{weight} kg is equal to {covert_in_pounds} pounds")
elif unit == "pounds":
    convert_in_kg = weight / 2.20462
    print(f"{weight} pounds is equal to {convert_in_kg} kg")
else:
    print("Invalid unit.")