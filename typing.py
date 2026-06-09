from time import time
import random as r

def mistake(par_test, usertest):
    error = 0
    for i in range(len(par_test)):
        try:
            if par_test[i] != usertest[i]:
                error += 1
        except IndexError:
            error += 1
    return error

def speed_time(time_start, time_end, user_input):
    time_delay = time_end - time_start
    if time_delay == 0:
        return 0
    speed = len(user_input.split()) / time_delay   # words per second
    return round(speed, 2)

# Test sentences
test = [
    "Hello! My name is Skyler Onyx. What is your name? I am studying in 9th grade.",
    "I am from Rajanpur, Punjab.",
    "Welcome to my test."
]

test1 = r.choice(test)

print("💖 Welcome to this typing test!")
print()
print(test1)
print()

# Start timing
time_1 = time()
user_input = input("Enter: ")
time_2 = time()

# Results
print()
print("Speed:", speed_time(time_1, time_2, user_input), "W/S")
print("Errors:", mistake(test1, user_input))