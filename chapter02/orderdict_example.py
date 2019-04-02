from collections import OrderedDict

# Make a OrderedDict
colors = OrderedDict()

# Assing values
colors["orange"] = "ORANGE"
colors["blue"] = "BLUE"
colors["green"] = "GREEN"

# Get values
[k for k, v in colors.items()]
# >>> ["orange", "blue", "green"]
