
file_name = input()

# Received r, h, cup_volume and glass_volume as floating point numbers from the user,
# DO NOT write any prompt messages inside the input functions.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

file = open(file_name)

r = float(file.readline())
h = float(file.readline())
cup_volume = float(file.readline())
glass_volume = float(file.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
print("r: %.2f, h: %.2f" % (r, h))

import math

# Define the required functions in the following section.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def calculate_cylinder_base_area():
    return 3 * (r**2)

def calculate_cylinder_lateral_area():
    return 2 * 3 * r * h

def calculate_cylinder_volume():
    return 3 * (r**2) * h

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

print("Cylinder's base area: %.2f" % (calculate_cylinder_base_area()))

# display how many times we should use the cylinder (which has its base removed) to fill the cup fully
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

cylinder_volume = calculate_cylinder_volume()
print(cup_volume / cylinder_volume)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

# display what percentage of the cylinder's volume will be empty, shown as integer
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

print(int(((cylinder_volume % glass_volume) / cylinder_volume) * 100))

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
