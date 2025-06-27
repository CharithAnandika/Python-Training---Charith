import datetime

sri_lanks_offset = datetime.timezone(datetime.timedelta(hours=5,minutes=30))
now_sri_lanka = datetime.datetime.now(sri_lanks_offset)
print(f"current datetime in sri lanka: {now_sri_lanka}")