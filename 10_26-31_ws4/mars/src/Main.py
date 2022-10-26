
# read the 'file*.txt' entirely, convert the content of the file to an integer and store it as a variable
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

input_file_name = input()
with open(input_file_name) as f:
    number = int(f.read())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# read the 'integer*.txt' , convert the content of the file to an integer and store it as a variable
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

integer_file_name = input()
with open(integer_file_name) as f:
    integer = int(f.read(number))

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# print strings, according to the following instructions:
# 1. If the integer in seconds represents more than 1 year, print "More than 1 year"
# 2. If the integer in seconds represents more than 1 day, print "More than 1 day"
# Years and days are of Mars, 687 days and 25 hours, respectively.
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

if integer > 60*60*25*687:
    print('More than 1 year')
if integer > 60*60*25:
    print('More than 1 day')

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
