def linearSearch(arr, n, v):

    for i in range(0, n):
        if (arr[i] == v):
            return i 
    return -1

arr = [2,3,4,10,15]
v = 15
n = len(arr)

result = linearSearch(arr, n, v)
if(result == -1):
    print("The number is not in the array")
else:
    print("The element is present in the index", result)