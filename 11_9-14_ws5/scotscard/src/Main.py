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

# You can create the price variables below (e.g. student first payment is 2.1)
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

student_first = 2.1
student_second = 1.55
student_third = 0.80
student_monthly = 75.20
worker_first = 4.2
worker_second = 3.3
worker_third = 1.75
worker_monthly = 186.50

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# You can return True if the card type is 'Student' here ; return False if not
def is_student(card_type):
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if card_type == 'Student':
        return True
    else:
        return False

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# You can store your price variables if the card type is student here. (e.g. first payment is 3.74)
if is_student(card_type):
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    first, second, third, monthly = student_first, student_second, student_third, student_monthly

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
# You can store your price variables if the card type is worker here. (first payment is 7.67)
else:
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    first, second, third, monthly = worker_first, worker_second, worker_third, worker_monthly
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# Create the function calculate_saved_amount here. This function returns the saved amount (positive)
def calculate_saved_amount(individual_payment, monthly):
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    return abs(individual_payment - monthly)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# You can calculate if the individual payment is higher than monthly payment, with 1, 2 or 3 vehicles ('vasıta'), here and print accordingly.
# If the monthly service is cheaper, print 'Monthly service'
# Or if the pay-as-you-go system is cheaper, print 'Pay-as-you-go system'
# You are requested to print 3 times (one for 1 vehicle, one for 2 and one for 3) in this part
for i in range(1, 4):
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
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
    print("%.2f" % (calculate_saved_amount(individual_payment, monthly)))
