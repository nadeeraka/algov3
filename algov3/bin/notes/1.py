list1 = [1, 2, 3, 4, 1, 2, 3]


# x = [1, 2, 3]
# x.append([4, 5])
# gives you: [1, 2, 3, [4, 5]]

def sumOfDif(a):
    return list(map(lambda x: x * 2, a))


def filterOdd(a):
    return list(filter(lambda x: x / 2 == 1, a))

#https://stackoverflow.com/questions/3335268/are-object-literals-pythonic
# object litarals in python
# >>> from collections import namedtuple
# >>> L = namedtuple('literal', 'name age')(**{'name': 'John Smith', 'age': 23})
# or keyword arguments
#
# >>> L = namedtuple('literal', 'name age')(name='John Smith', age=23)
# >>> L
# literal(name='John Smith', age=23)
# >>> L.name
# 'John Smith'
# >>> L.age
