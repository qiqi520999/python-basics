"""
Tính số ngày, số tuần, số tháng, số giờ, số giây, số phút trong 27 năm
Note: đừng lo lắng về năm nhuận !
"""
years = 27

days = years * 365
weeks = 365 // 7
months = years * 12

hours = days * 24
minutes = hours * 60
seconds = minutes * 60

"""
Number of years: 27
<=>
Number of days: {days}
...
f-strings
"""
print(f"Number of years: {years}")
print("<=>")

print(f"Number of days: {days}")
print(f"Number of weeks: {weeks}")
print(f"Number of months: {months}")
print(f"Number of hours: {hours}")
print(f"Number of minutes: {minutes}")
print(f"Number of seconds: {seconds}")

"""
Note: variable: name for a value
f-strings
logic
"""
