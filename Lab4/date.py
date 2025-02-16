import datetime as dt
#task 1
x = dt.datetime.now()
a = dt.datetime(x.year, x.month, x.day - 5) 
print(a)

#task 2
yesterday = dt.datetime(x.year, x.month, x.day - 1)
today = dt.datetime.now()
tomorrow = dt.datetime(x.year, x.month, x.day + 1)

print(yesterday, today, tomorrow)
#task 3
print(today.strftime("%f"))
#task 4
Y, m, d, H, M, S = map(int, input("Enter first year, month, day, hour, minute, second: ").split())
date1 = dt(Y, m, d, H, M, S)
Y, m, d, H, M, S = map(int, input("Enter second: ").split())
date2 = dt(Y, m, d, H, M, S)
print(f'Difference is {(date2-date1).total_seconds()}')

