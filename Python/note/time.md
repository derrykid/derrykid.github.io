## Get current time since 1970
```python
import time
time.time()
```

## Pause with `Sleep()`

The @param is second, not millesecond!
```python
time.sleep(1)
```

## Datetime
`import datetime`

Get the time now
```python
dt = datetime.datetime.now()

>>> dt.year, dt.month, dt.day
   (2019, 10, 21)
>>> dt.hour, dt.minute, dt.second
   (16, 29, 0)
```

Print the current time
```python
>>> datetime.datetime.fromtimestamp(time.time())
datetime.datetime(2019, 10, 21, 16, 30, 0, 604980)
```

## timedelta data type - show the duration of time
```python
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
>>> delta.days, delta.seconds, delta.microseconds
   (11, 36548, 0)
>>> delta.total_seconds()
986948.0
>>> str(delta)
'11 days, 10:09:08'
```

Add days to the time given:
```python
>>> dt = datetime.datetime.now()
>>> dt
datetime.datetime(2018, 12, 2, 18, 38, 50, 636181)
>>> thousandDays = datetime.timedelta(days=1000)
>>> dt + thousandDays
datetime.datetime(2021, 8, 28, 18, 38, 50, 636181)
```

Even, subtract the day:
```python
>>> oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
>>> aboutThirtyYears = datetime.timedelta(days=365 * 30)
>>> oct21st
datetime.datetime(2019, 10, 21, 16, 29)
>>> oct21st - aboutThirtyYears
datetime.datetime(1989, 10, 28, 16, 29)
>>> oct21st - (2 * aboutThirtyYears)
datetime.datetime(1959, 11, 5, 16, 29)
```

## Convert datetime objects

- strftime() - format time
- strptime() - parse time

| directive | Meaning                             |
|-----------|-------------------------------------|
| %Y        | Year with century, '2014'           |
| %y        | Year w/o century, '14'              |
| %m        | month as decimal, 01 to 12          |
| %B        | Full month, 'November'              |
| %b        | 'Nov'                               |
| %d        | Day, '01' to '31'                   |
| %j        | Day of the year, '001' to '366'     |
| %w        | Day of the week, '0' Sun to '6' Sat |
| %A        | Weekday name, 'Monday'              |
| %a        | 'Mon'                               |
| %H        | Hour, '00' to '23'                  |
| %I        | 12-hr clock, '01' to '12'           |
| %M        | Minute, '00' to '59'                |
| %S        | Second, '00' to '59'                |
| %p        | 'AM' or 'PM'                        |
| %%        | Literal '%' character               |

strftime(): string
```python
>>> oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
>>> oct21st.strftime('%Y/%m/%d %H:%M:%S')
'2019/10/21 16:29:00'
>>> oct21st.strftime('%I:%M %p')
'04:29 PM'
>>> oct21st.strftime("%B of '%y")
"October of '19"
```

Convert date to `datetime` with `strptime`
```python
datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')
datetime.datetime(2019, 10, 21, 0, 0)
datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
datetime.datetime(2019, 10, 21, 16, 29)
datetime.datetime.strptime("October of '19", "%B of '%y")
datetime.datetime(2019, 10, 1, 0, 0)
datetime.datetime.strptime("November of '63", "%B of '%y")
datetime.datetime(2063, 11, 1, 0, 0)
```

## Get day (Mon, etc) of the week 
```python
# target January 7, 2019
day = datetime.datetime(2019, 1, 7).weekday()
print(day) # give use 0, means it's Monday
```
