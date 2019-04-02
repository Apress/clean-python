
from collections import namedtuple

# Make a namedtuple
Company = namedtuple("Company", ["name", "employee", "location"])

# Assing values
company = Company("google", 50000, "MountainView")

# Get values
company.name
#>>> google
company.employee
#>>> 50000
company.location
#>>> MountainView
