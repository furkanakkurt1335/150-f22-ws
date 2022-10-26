
file_name = input()

# Received hours_in_shinsoo_day as integer point numbers from the user,
# DO NOT write any prompt messages inside the input functions.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

file = open(file_name)

hours_in_shinsoo_day = int(file.readline())
days_in_shinsoo_year = int(file.readline())
counter = int(file.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
import math


# Calculate how many Shinsoo years, how many Shinsoo days, how many hours, minutes and second he has been on Shinsoo, respectively, and print them as "integer" on separate lines
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

one_minute = 60
one_hour = 60*60
one_day = one_hour*hours_in_shinsoo_day
one_year = one_day*days_in_shinsoo_year

print(int(counter / one_year))
remaining_seconds_from_year = counter%one_year
print(int(remaining_seconds_from_year / one_day))
remaining_seconds_from_day = counter%one_day
print(int(remaining_seconds_from_day / one_hour))
remaining_seconds_from_hour = counter%one_hour
print(int(remaining_seconds_from_hour / one_minute))
remaining_seconds_from_minute = counter%one_minute
print(int(remaining_seconds_from_minute))

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

# If he has been on Shinsoo for more than or equal to 1 Shinsoo century (100 Shinsoo years), print "longer than a Shinsoo century" on the separate line.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

if(counter / one_year) >= 100 :
    print("longer than a century")

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
