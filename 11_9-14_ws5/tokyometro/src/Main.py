# Read the type of card string and the integer for the day count from the file
# Please use the `strip` function for removing any whitespace characters ('\n', ' ', etc.) from the string in the first line (Student or Worker)
# `strip` example usage:
#   our_string = ' String with new line \n'
#   string_stripped = our_string.strip()
# our_string is now 'String with new line'.

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

filename = input()
f = open(filename, 'r')
card_type = f.readline().strip()
day_count = int(f.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# You can create the price variables below (e.g. for a student, 3 stations or less is 400)
# You can define a function to return True if the card type is 'Student' here ; return False otherwise
# You can store your price variables if the card type is student or worker here. (e.g. 3 stations or less is 400 for students and 800 for workers)

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

student_three = 400
student_six = 600
student_nine = 750

worker_three = 800
worker_six = 1200
worker_nine = 1500

def is_student(card_type):
    if card_type == 'Student':
        return True
    else:
        return False

if is_student(card_type):
    three, six, nine = student_three, student_six, student_nine
else:
    three, six, nine = worker_three, worker_six, worker_nine

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# You can print here: how much money they pay for all 3 cases of usage (3 stations or less, 4 to 8 stations or, 9 or more stations) in separate lines.
# You are expected to define a for loop in this section
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

for i in range(1, 4):

    if i == 1:
        print(three*day_count*2)

    elif i == 2:
        print(six*day_count*2)

    else:
        print(nine*day_count*2)


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
