import datetime

time = datetime.datetime.now()
str_time = time.strftime('%Y/%m/%d %H:%M:%S')

with open('debug.txt', 'a') as f:
    print(str_time+': setup.py called', file=f)
