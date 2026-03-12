import datetime

date = "Jan 15, 2023 - 12:05:33"

date_task = datetime.datetime.strptime(date, "%b %d, %Y - %H:%M:%S")

print(date_task.strftime("%B"))
print(date_task.strftime("%d.%m.%Y, %H:%M"))
