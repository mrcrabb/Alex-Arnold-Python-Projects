#Name: Alex Arnold Year:2024
#Assignment: Calander Project
#================================>
#Description:
''''
In this assignment I want make a functioning calander
'''
#================================>
import calendar
import datetime

# Get the current month and year
now = datetime.datetime.now()
month = now.month
year = now.year

# Create a calendar object
cal = calendar.monthcalendar(year, month)

# Print the calendar
print("  Sun Mon Tue Wed Thu Fri Sat")
for week in cal:
    for day in week:
        if day == 0:
            print("   ", end="")
        else:
            print(f"{day:3}", end="")
    print()
