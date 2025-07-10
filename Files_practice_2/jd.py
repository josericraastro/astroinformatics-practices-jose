day = int(input("Write the day: (1-31): "))
month = int(input("Write the month: (1-12): "))
year = int(input("Write the year:(ex. 2008): "))

if month == 1 or month == 2:
    month += 12  # January -> 13, February-> 14
    year -= 1  # the year is reduced

julian_day = (36525 * year) // 100 + (306001 * (month + 1)) // 10000 + day + 1720981


print("The julian day is:", julian_day)
