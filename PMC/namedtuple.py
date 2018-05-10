# pt1 = (1.0, 5.0)
# pt2 = (2.5, 1.5)
#
# from math import sqrt
# line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

from collections import namedtuple
from math import sqrt

x = namedtuple('x', ['x', 'y'])
pt1 = x(1.0, 5.0)
pt2 = x(2.5, 1.5)


# line_length = sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2)

print(help(namedtuple))
print(pt1.x, pt1.y)
print(pt2.x, pt2.y)
