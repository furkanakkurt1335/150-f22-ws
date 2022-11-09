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

# You can create the price variables below (e.g. student first payment is 3.74) if you need to
# You can set your price variables if the card type is student or worker here.
# (e.g. first payment is 3.74 for student, 7.67 for worker)

# You can define a function that returns True if the card type is 'Student' here ; return False otherwise
# Also define the function calculate_saved_amount here. This function returns the saved amount (positive)

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

student_first = 3.74
student_second = 1.64
student_third = 1.54
student_monthly = 109

worker_first = 7.67
worker_second = 5.49
worker_third = 4.17
worker_monthly = 602

def is_student(card_type):
    if card_type == 'Student':
        return True
    else:
        return False

def calculate_saved_amount(individual_payment, monthly):
    return abs(individual_payment - monthly)

if is_student(card_type):
    first, second, third, monthly = student_first, student_second, student_third, student_monthly

else:
    first, second, third, monthly = worker_first, worker_second, worker_third, worker_monthly

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# You can calculate if the individual payment is higher than monthly payment, with 1, 2 or 3 vehicles ('vasıta'), here and print accordingly.
# If the monthly service is cheaper, print 'Monthly service'
# Or if the pay-as-you-go system is cheaper, print 'Pay-as-you-go system'
# You are requested to print 3 times (one for 1 vehicle, one for 2 and one for 3) in this part


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
for i in range(1, 4):

    if i == 1:
        individual_payment = (day_count*first)*2

    elif i == 2:
        individual_payment = (day_count*(first+second))*2

    else:
        individual_payment = (day_count*(first+second+third))*2

    if individual_payment < monthly:
        print('Pay-as-you-go system')

    else:
        print('Monthly service')

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

    # We print the saved amount, whatever the choice is (monthly or pay-as-you-go)
    # You are expected to define a for loop in the section above,
    # so the following line is indented intentionally to be executed within the for loop body.

    print("%.2f" % (calculate_saved_amount(individual_payment, monthly)))
