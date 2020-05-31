# o some whole positive number we need to print out all the numbers from 1 to that number.
# So when I say print out I really mean console logs we are going to cancel log out all the numbers from
# 1 to n. However for any number that is a multiple of three it's a multiple of three.
# We are going to print out the string fills.
# If the number is a multiple of five we're going to print out because if the number is a multiple of
# both 3 and 5 then we're going to print out fizz buzz.
# That's it.


def clasicFizBuz(n):
    a = []
    for i in range(0, n+1):
        if i % 3 == 0:
            a.append('Fiz')
        elif i % 5 == 0:
            a.append('Buz')
        elif i % 3 == 0 and n % 5 == 0:
            a.append('FizBuzz')
    return a
print(clasicFizBuz(10))