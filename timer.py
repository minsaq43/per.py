import time

my_time = int(input("Enter the time in seconds: "))
for x in reversed(range(0,my_time)):
    seconds = x % 60
    minutes = x // 60
    hours  = x // 3600
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)
print("Time's up!")