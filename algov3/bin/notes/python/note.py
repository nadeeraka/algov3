# They are all similar, Lamdba functions are often passed as a parameter to these functions in python.
#
# Reduce:
#
#  >>> from functools import reduce
#  >>> reduce( (lambda x, y: x + y), [1, 2, 3, 4]
#  10
# Filter:
#
# >>> list( filter((lambda x: x < 0), range(-10,5)))
# [-10, -9, -8, -7, - 6, -5, -4, -3, -2, -1]
# Map:
#
# >>> list(map((lambda x: x **2), [1,2,3,4]))
# [1,4,9,16]