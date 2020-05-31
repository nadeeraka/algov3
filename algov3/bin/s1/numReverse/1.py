# -12 =>-21

def numberReverse(num):
    isLow = False
    if num < 0:
        isLow = True
    toStr = str(num)
    arr = list(toStr)
    return arr.reverse()
    

print(numberReverse(12))
