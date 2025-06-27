import datetime

now = datetime.datetime.now()

future_date = now + datetime.timedelta(days=7)
print(f"7 days from now : {future_date}")

past_time = now - datetime.timedelta(hours=3)
print(f"3 hours ago : {past_time}")

date1 = datetime.datetime(1995,7,16)
date2 = datetime.datetime(2025,6,27)
difference = date2 - date1
print(f"differnce between dates : {difference}")
print(f"difference in days : {difference.days}")