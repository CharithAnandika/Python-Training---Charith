import time

def long_task():
    print("Long task : Starting...(This will take 3 seconds)")
    time.sleep(3) #simulate a 3-second wait
    print("Long task : Finished!")

def short_task():
    print("short task : running quickly")
    time.sleep(0.5) #simulate a 0.5-second wait
    print("short task : Finished!")

print("---Program without thread---")

long_task()

short_task()

print("---Program without thread done---")