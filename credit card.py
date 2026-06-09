sun_odd_digit = 0
sum_even_digit = 0
total =0

#step 1
card_number = input("Enter your credit card number: ")
card_number = card_number.replace(" ", "")
card_number = card_number.replace("-", "")
card_number = card_number[::-1]
print("Card number:" , card_number)
#step 2
for x in card_number[::2]:
    sum_odd_digit += int(x)
# step 3
for x in card_number[1::2]:
    x = int(x) * 2
    if x > 10:
        sum_even_digit += (1 + (x % 10))
    else:
        sum_even_digit += x
# step 4
total = sum_odd_digit + sum_even_digit
# step 5
if total % 10 == 0:
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")