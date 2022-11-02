
file_name = input()

# Receive first_mass, second_mass, distance as integer numbers from the user
# DO NOT write any prompt messages inside the input functions.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

file = open(file_name)

first_mass = int(file.readline())
second_mass = int(file.readline())
distance = int(file.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

import math


# Print the magnitude of gravitational force as an integer number
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

gravitational_force = (first_mass * second_mass) / (distance * distance)
print(int(gravitational_force))

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
# If the magnitude of gravitational force is greater than or equal to the sum of all inputs, print "greater than or equal to the sum".
# Else if the magnitude of gravitational force is greater than or equal to one tenth of the sum of all inputs, print "greater than or equal to one tenth of the sum".
# Else, print "less than one tenth of the sum"
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

if gravitational_force >= (first_mass + second_mass + distance):
    print("greater than or equal to the sum")
    
elif gravitational_force >= (first_mass + second_mass + distance)/10:
    print("greater than or equal to one tenth of the sum")
    
else:
    print("less than one tenth of the sum")

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
