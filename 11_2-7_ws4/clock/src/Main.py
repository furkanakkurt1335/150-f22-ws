
# Read the first file (<i>'time*.txt'</i>) entirely. This file's content represents time of a day as a string (e.g. '1050' meaning 10:50 AM, using a 24-hour system). Convert it to an integer and perform operations to store the time's hour and minute values in 2 different variables.
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

input_file_name = input()
with open(input_file_name) as f:
    time = int(f.read())
hour, minutes = time // 100, time % 100

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# Read the second file (<i>'offset*.txt'</i>). This file's content represents seconds. Store it in a variable as an integer.
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

offset_file_name = input()
with open(offset_file_name) as f:
    offset = int(f.read())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# Calculate what the time (given in the first file) would be after adding the seconds (given in the second file) to it. Print a string, according to the following instructions:
# If the resultant time is before noon (12:00), print "Before noon".
# If the resultant time is after noon (12:00), print "After noon".
# If the resultant time is just noon (12:00), print "High noon".
# In the end, only 1 line will be printed.
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

year_len = 365
week_len = 7
day_len = 24
hour_len = 60
min_len = 60

res_hour = (hour + (offset // (min_len*hour_len))) % 24
res_min = (minutes + (offset // (min_len))) % 60
if res_min <= minutes:
    res_hour += 1

if res_hour > 12:
    print('After noon')
elif res_hour < 12:
    print('Before noon')
elif res_hour == 12:
    if res_min == 0:
        print('High noon')
    else:
        print('After noon')

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
