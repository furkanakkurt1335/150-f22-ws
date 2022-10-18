
file_name = input()

# Received h,l,d,r,k,y,x,n as floating point numbers from the user,
# DO NOT write any prompt messages inside the input functions.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

file = open(file_name)

h = float(file.readline())
l = float(file.readline())
d = float(file.readline())
r = float(file.readline())
k = float(file.readline())
y = float(file.readline())
x = float(file.readline())
n = float(file.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
print("h: %.2f, l: %.2f, d: %.2f, r: %.2f, k: %.2f, y: %.2f, x: %.2f, n: %.2f" % (h,l,d,r,k,y,x,n) )

import math

# Define the required functions in the following section.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def calculate_container_base_area():
    return 3 * (r**2)

def calculate_container_volume():
    return 3 * (r**2) * k

def calculate_pot_volume():
    return h * l * d

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

print(calculate_container_base_area())
print(calculate_container_volume())
print(calculate_pot_volume())

# Display how many pots of hummus do you need to have hummus for all of the students
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

container_volume = calculate_container_volume()
pot_volume = calculate_pot_volume()
print((container_volume / pot_volume)*(y*x/100))

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

# display the total cost of the schnitzel to the cafeteria
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

print((y*(100-x)/100)*2*n)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
