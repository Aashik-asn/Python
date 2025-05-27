# Get input from user
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

# Number of days in each month
month_days = [31, 28, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]

# Check leap year and update February
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    month_days[1] = 29  # February has 29 days in a leap year

# Move to next day
day += 1

if day > month_days[month - 1]:
    day = 1
    month += 1
    if month > 12:
        month = 1
        year += 1

# Print tomorrow's date
print("Tomorrow's date: {}-{}-{}".format(day, month, year))
