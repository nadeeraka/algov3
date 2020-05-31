
ar = [1,2,3,4,5]

# Using an additional state variable, such as an index variable (which you would normally use in languages such as C or PHP), is considered non-pythonic.
# The better option is to use the built-in function enumerate(), available in both Python 2 and 3:
# for idx, val in enumerate(ints):
#     print(idx, val)

def chunk(arr,size):
    newAr = []
    for i in range(len(arr)):
        print(i, ':', arr[i])
        

print(chunk(ar,2))
        