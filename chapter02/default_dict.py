from collections import defaultdict

# Make a defaultdict
colors = defaultdict(int)

# Try printing value of non-existing key would give us default values
colors["orange"]
# >>> 0

print(colors)
# >>> defaultdict(int, {"orange": 0})
