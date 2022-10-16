
file_name = input()

# Received r, h, cup_volume and glass_volume as floating point numbers from the user,
# DO NOT write any prompt messages inside the input functions.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

file = open(file_name)

r = float(file.readline())
cup_volume = float(file.readline())
glass_volume = float(file.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
print("r: %.2f" % (r))

import math

# Define the required functions in the following section.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def  calculate_sphere_diameter():
    return 2 * r

def calculate_sphere_area():
    return 4 * 3 * (r**2)

def calculate_sphere_volume():
    return 4 / 3 * 3 * (r**3)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

print("Sphere's area: %.2f" % (calculate_sphere_area()))

# display how many times we should use the half-sphere to fill the cup fully
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

halfsphere_volume = calculate_sphere_volume() / 2
print(cup_volume / halfsphere_volume)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

# display what percentage of the half-sphere's volume will be empty, shown as integer
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

print(int(((halfsphere_volume % glass_volume) / halfsphere_volume) * 100))

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
