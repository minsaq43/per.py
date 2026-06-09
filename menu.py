menu = {
    "pizza": 10.9,
    "burger": 8.5,
    "salad": 6.25,
    "soda": 2.0,
    "fries": 3.5,
    "lemonade": 4.0
    ,"ice cream": 5.0
}
cart = []
total = 0

print("Welcome to the restaurant! Here's our menu:")
for key, value in menu.items():
    print(f"{key}: ${value}")

while True:
    food = input("Which food you like to buy (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total  += menu.get(food)
    print(food , end= " ")
print()
print(f"Your total is: ${total:.2f}")