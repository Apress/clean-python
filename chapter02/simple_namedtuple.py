import namedtuple


Point = namedtuple("Point", ["x", "y", "z"])
point = Point(x=3, y=4, z=5)
point.x
point.y
point.z
