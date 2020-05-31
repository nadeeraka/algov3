# -12 =>-21

def numberReverse(num):
    isLow = False
    if num < 0:
        isLow = True
    toStr = str(num)
    arr = list(reversed(toStr))
    if isLow:
      del  arr[-1]
      arr.insert(0,'-')
    str1 =''
    return int(str1.join(arr))
   
print(numberReverse(-12))
