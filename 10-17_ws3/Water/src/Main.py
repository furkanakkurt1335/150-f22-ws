
file_name = input()

# Received container_height, container_base_height, glass_base_radius, glass_height and student_count floating point numbers from the user,
# DO NOT write any prompt messages inside the input functions.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

file = open(file_name)

container_height = float(file.readline())
container_base_edge = float(file.readline())
glass_base_radius = float(file.readline())
glass_height = float(file.readline())
student_count = float(file.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
print("container_height: %.2f, container_base_edge: %.2f, glass_base_radius: %.2f, glass_height: %.2f, student_count: %.2f" % (container_height, container_base_edge, glass_base_radius, glass_height, student_count))

import math

# Define the required functions in the following section.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def calculate_container_base_area():
    return (container_base_edge**2)

def calculate_glass_volume():
    return 3*(glass_base_radius**2)*glass_height

def calculate_container_volume():
    return (container_base_edge**2)*container_height

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

print(calculate_container_base_area())
print(calculate_glass_volume())
print(calculate_container_volume())

# How many liters of water does each student drink per day? Print the value.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

print(calculate_glass_volume()*10)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
# These containers are filled with water once a day. How many containers are needed for enough water for all the students? Print the value.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

print((calculate_glass_volume() * 10 * student_count) / calculate_container_volume())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
