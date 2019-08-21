from datetime import date, datetime, timedelta

day = date.today()
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
test = datetime.strptime("2018-11-22 00:00:00","%Y-%m-%d %H:%M:%S")
print(now)
print(test)
# delta = timedelta(days=5)
# n_days_after = now + delta
# n_days_forward = now - delta
# print(("当前日期：{}").format(now))
# print("向后推迟5天的日期：{}".format(n_days_after.strftime('%Y-%m-%d %H:%M:%S')))
# print("向前推5天的日期：{}".format(n_days_forward.strftime('%Y-%m-%d')))