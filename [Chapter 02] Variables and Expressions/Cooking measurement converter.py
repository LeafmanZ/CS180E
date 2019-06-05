
# FIXME (1): Finish reading other items into variables, then output the three ingrdients
lemon = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n\n'))
lemon_serv = lemon/servings
water_serv = water/servings
agave_serv = agave/servings
print('Lemonade ingredients - yields %.2f servings' % servings)
print('%.2f cup(s) lemon juice' % lemon)
print('%.2f cup(s) water' % water)
print('%.2f cup(s) agave nectar\n' % agave)
# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
serving_make = float(input('How many servings would you like to make?\n\n'))
print('Lemonade ingredients - yields %.2f servings' % serving_make)
print('%.2f cup(s) lemon juice' % (lemon_serv*serving_make))
print('%.2f cup(s) water' % (water_serv*serving_make))
print('%.2f cup(s) agave nectar\n' % (agave_serv*serving_make))
# FIXME (3): Convert and output the ingredients from (2) to gallons
print('Lemonade ingredients - yields %.2f servings' % serving_make)
print('%.2f gallon(s) lemon juice' % (lemon_serv*serving_make/16))
print('%.2f gallon(s) water' % (water_serv*serving_make/16))
print('%.2f gallon(s) agave nectar' % (agave_serv*serving_make/16))
