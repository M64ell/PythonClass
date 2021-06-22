import math
#macaw problem
carrying_weight_percentage = 1/3
grams_per_macaw = 900/3
coconuts_mass = 1450
macaw_weight = 900
total_macaws_needed = 1450/grams_per_macaw
print(math.ceil (total_macaws_needed))
macaw_limit = macaw_weight * carrying_weight_percentage
number_macaws = coconuts_mass/macaw_limit
print(math.ceil(number_macaws))