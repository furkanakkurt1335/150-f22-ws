# Read the type of card string and both of the integers (day and vehicle counts) from the file
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

filename = input()
f = open(filename, 'r')
student_worker = f.readline().strip()
day_count = int(f.readline())
vehicle_count = int(f.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# You can create the price variables below
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

student_first = 3.74
student_second = 1.64
student_third = 1.54
student_monthly = 109
worker_first = 7.67
worker_second = 5.49
worker_third = 4.17
worker_monthly = 602

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# Print as follows:
# If the monthly service is better, print 'Monthly service'
# Or if the pay-as-you-go system is better, print 'Pay-as-you-go system'
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

if student_worker == 'Student':
    first, second, third, monthly = student_first, student_second, student_third, student_monthly
else:
    first, second, third, monthly = worker_first, worker_second, worker_third, worker_monthly
if vehicle_count == 1:
    individual_payment = (day_count*first)*2
elif vehicle_count == 2:
    individual_payment = (day_count*(first+second))*2
else:
    individual_payment = (day_count*(first+second+third))*2
if individual_payment < monthly:
    print('Pay-as-you-go system')
else:
    print('Monthly service')

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# Create the function calculate_saved_amount here
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def calculate_saved_amount(individual_payment, monthly):
    return abs(individual_payment - monthly)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
# We print the saved amount, whatever the choice is (monthly or pay-as-you-go)
print("%.2f" % (calculate_saved_amount(individual_payment, monthly)))
