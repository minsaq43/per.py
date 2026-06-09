principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter the principle: "))
    if principle <= 0:
        print("Interest should not be negative or equal to zero.")

while rate <=0:
    rate = int(input("Enter the rate: "))
    if rate <= 0:
        print("Rate should not be negative or equal to zero.")

while time <=0:
    time = int(input("Enter the time: "))
    if time <= 0:
        print("Time should be in years")
user_input = input("Which type of interest do you want to calculate? (simple/compound): ")
if user_input == "simple":
    simple_interest = (principle * rate *time) / 100
    print(f"Simple Interest: {simple_interest}")
elif user_input == "compound":
    compound_interest = principle * (pow((1 + rate / 100)))