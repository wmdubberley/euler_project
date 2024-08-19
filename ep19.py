from util import is_leap_year

def count_sundays_on_first():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = 1  # 1 Jan 1900 was a Monday, so day_of_week = 1 means Monday
    sunday_count = 0

    # Start counting from 1 Jan 1901
    for year in range(1900, 2001):
        for month in range(12):
            if year >= 1901:
                # Check if the first of the month is a Sunday
                if day_of_week % 7 == 0:
                    sunday_count += 1

            # Move to the next month
            days = days_in_month[month]
            if month == 1 and is_leap_year(year):  # Adjust for leap year in February
                days += 1

            day_of_week += days

    return sunday_count

# Calculate the number of Sundays on the first of the month during the 20th century
result = count_sundays_on_first()
print(f"The number of Sundays that fell on the first of the month during the 20th century is: {result}")
