# Read the file
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

filename = input()
f = open(filename, 'r')
# money sum
money = int(f.readline())
# percents
apple_amount = int(f.readline())
banana_amount = int(f.readline())
carrot_amount = int(f.readline())
# diet
protein_requirement = int(f.readline())
fat_requirement = int(f.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

apple_cost = 4
banana_cost = 12
carrot_cost = 3

# This function returns the price of the item
def get_price(amount, cost):
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    return amount * cost
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# This function returns True if the money is enough to buy the items ; otherwise, returns False
def is_affordable(money, apple_amount, apple_cost, banana_amount, banana_cost, carrot_amount, carrot_cost):
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    return money >= get_price(apple_amount, apple_cost) + get_price(banana_amount, banana_cost) + get_price(carrot_amount, carrot_cost)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# This function returns the units fulfilled by the `amount`
def get_fulfillment(amount, unit_mg):
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    return unit_mg * amount
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# This function returns True if the requirement is fulfilled ; otherwise, returns False
def is_fulfilled(requirement, apple_amount, apple_mg, banana_amount, banana_mg, carrot_amount, carrot_mg):
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    return get_fulfillment(apple_amount, apple_mg)+ get_fulfillment(banana_amount, banana_mg) + get_fulfillment(carrot_amount, carrot_mg) >= requirement
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

apple_protein = 10
apple_fat = 3
banana_protein = 12
banana_fat = 8
carrot_protein = 9
carrot_fat = 4

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

if is_affordable(money, apple_amount, apple_cost, banana_amount, banana_cost, carrot_amount, carrot_cost):
    if is_fulfilled(protein_requirement, apple_amount, apple_protein, banana_amount, banana_protein, carrot_amount, carrot_protein):
        if is_fulfilled(fat_requirement, apple_amount, apple_fat, banana_amount, banana_fat, carrot_amount, carrot_fat):
            print('Enough protein and fat consumed')
        else:
            print('Enough protein consumed but not enough fat consumed.')
    elif is_fulfilled(fat_requirement, apple_amount, apple_fat, banana_amount, banana_fat, carrot_amount, carrot_fat):
        print('Enough fat consumed but not enough protein consumed.')
    else:
        print('Not enough protein or fat consumed.')
else:
    print('Not enough money.')

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
