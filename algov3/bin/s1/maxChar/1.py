s = 'abcccc'


def maxChar(str):
    myObj = dict()
    val = 0
    if len(str) < 0:
        return -1
    arr = list(str)
    for i in arr:
        if i in myObj:
            myObj[i] += 1
        else:
            myObj[i] = 1
        for i in myObj:
            if val < myObj[i]:
                val = myObj[i]
       
       
    return [number for number, i in myObj.items() if i == val]


print(maxChar(s))
