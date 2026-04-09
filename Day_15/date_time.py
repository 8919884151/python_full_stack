
from datetime import date,time,datetime,timedelta
'''today=date.today() #today date
print(today)
print(date(2026,3,31)) #date format
print(today.year)
print(today.month)
print(today.day)
print(today.weekday()) #0=monday and 6=sunday
print(today.isoweekday())  #1=monday and 7=sunday
time=time(16,41,56)
print(time)
print(time.hour)
print(time.minute)
print(time.second)

now=datetime.now()
print(now)#2026-04-02 16:51:28.695754
print(now.strftime("%d-%m-%Y %H:%M:%S"))#02-04-2026 16:51:28
print(now.strftime("%d/%m/%Y %H:%M:%S"))#02/04/2026 16:51:28
print(now.strftime("%d-%b-%Y %H:%M:%S"))#02-Apr-2026 16:51:28
print(now.strftime("%d-%B-%Y %H:%M:%S"))#02-April-2026 16:51:28
print(now.strftime("%d-%m-%Y %I:%M:%S"))#02-04-2026 04:51:28
print(now.strftime("%d-%m-%Y %H:%M:%S %p"))#02-04-2026 16:51:28 PM
print(now.strftime("%A,%d-%m-%Y %H:%M:%S"))#Thursday,02-04-2026 16:51:28'''

today=date.today()
now=datetime.now()
result=today+timedelta(days=2)
print(result)
result1=now-timedelta(hours=2)
print(result1)


