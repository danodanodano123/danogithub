import time
start=int(input("Enter the starting time for the countdown: "))
while start>=0:
    print(start)
    time.sleep(1)
    start-=1
print("Countdown complete")