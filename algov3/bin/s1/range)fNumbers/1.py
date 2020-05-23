# Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
#
# Note: a and b are not ordered!
#
# Examples
# get_sum(1, 0) == 1   // 1 + 0 = 1
# get_sum(1, 2) == 3   // 1 + 2 = 3
# get_sum(0, 1) == 1   // 0 + 1 = 1
# get_sum(1, 1) == 1   // 1 Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1
# get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

def sumOfAllTheNum(a,b):
    count = 0
    if a> b:
        x = range(a-1,b-1)
    else:  x = range(b-1,a-1)

    for i in x:
        count += i
    return count

print(sumOfAllTheNum(1,3))
