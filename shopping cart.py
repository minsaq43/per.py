
foods = []
prices = []
total = 0
while True:
    food = input("Enter a food you wanna to buy (q for quit): ")
    if food.lower() =="q":
        break
    else:
        price = float(input("Enter the price of the food: $"))
        foods.append(food)
        prices.append(price)
        total += price

print(f"Your total is: ${total:.2f}")