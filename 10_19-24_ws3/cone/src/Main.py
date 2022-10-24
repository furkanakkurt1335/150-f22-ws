
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

def  calculate_cone_base_area():
    return 3 * (r**2)

def calculate_cone_lateral_area():
    return 3 * r * math.sqrt(h**2 + r**2)

def calculate_cone_volume():
    return 3 * (r**2) * h / 3

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

print("Cone's base area: %.2f" % (calculate_cone_base_area()))

# display how many times we should use the cone (which has its base removed) to fill the cup fully
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

cone_volume = calculate_cone_volume()
print(cup_volume / cone_volume)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

# display what percentage of the cone's volume will be empty, shown as integer
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

print(int(((cone_volume % glass_volume) / cone_volume) * 100))

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
