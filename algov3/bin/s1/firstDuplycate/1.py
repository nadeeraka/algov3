
#  return first duplicate in given array

l = [1, 0, 8, 2, 3]


def firstRe(parameter_list):
    obj = dict()
    if (type(parameter_list) != list) and (len(parameter_list) < 0):
        return -1
    for i in parameter_list:
        if i in obj:
            return i
        obj[i] = i

    return None


print(firstRe(l))
