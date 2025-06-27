import datetime

now = datetime.datetime.now()
print(f"current datetime : {now}")

today = datetime.date.today()
print(f"current date : {today}")

curent_time = now.time()
print(f"current time : {curent_time}")

print(f"Year : {now.year}")
print(f"month : {now.month}")
print(f"day : {now.day}")
print(f"hour : {now.hour}")
print(f"min : {now.minute}")
print(f"sec : {now.second}")
print(f"micsec : {now.microsecond}")
print(f"weekday : {now.weekday()}")#(monday =0)