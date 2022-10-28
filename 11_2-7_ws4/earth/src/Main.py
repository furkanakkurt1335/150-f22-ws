
# Read the 'file*.txt' entirely, convert the content of the file to an integer and store it as a variable.
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

input_file_name = input()
with open(input_file_name) as f:
    number = int(f.read())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# read the 'integer*.txt' file, convert the content of the file to an integer and store it as a variable.
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

integer_file_name = input()
with open(integer_file_name) as f:
    integer = int(f.read(number))

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# Print strings, according to the following instructions:
# If the integer in seconds represents less than or equal to 1 day, print "Less than 1 day".
# If the integer in seconds represents more than 1 day, print "More than 1 day".
# If the integer in seconds represents more than 1 year, print "More than 1 year". Do not print "More than 1 day".
# Years and days are of Earth, 365 days and 24 hours, respectively. In the end, only 1 line will be printed.
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

year_length = 365
day_length = 24

if integer > 60*60*day_length*year_length:
    print('More than 1 year')
elif integer > 60*60*day_length:
    print('More than 1 day')
else:
    print('Less than 1 day')

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
