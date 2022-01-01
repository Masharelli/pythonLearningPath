# Welcome to the my Learning Path of Python

Hi devs here **Masha**!



This repository it's very personal and important, because I'm in my last semester of the University and I set a personal goal.

 **Be a Python Developer to get in a big tech company !!!**

## **Personal Experience**

Actually right now I'm a Application developer at IBM, working with API's in **Spring Boot(JAVA)** also working with a little bit of **Scala** and **Spark**

### **Style Guide (PEP8)**

In this repositorie or course, I´ll using the guide style for python **PEP8** so the following code will be in this format.
[PEP8 Guide Link](https://www.python.org/dev/peps/pep-0008/)

### **Algorithms study**

#### **Insertion Sort** 
This algorithm work to sort an array of numbers this is working with small quantity of numbers.
- **Time complexity it´s of: O(n^2)** 
- **Auxiliary Space: O(1)**

### **Code in Python (Example)**
    def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    for i in range(len(arr)):
    print ("% d" % arr[i])

Case when you want to sort the array in **decrease** way 

    def insertionSortDecrease(arr):

    for i in range(1, len(arr)):
        key = arr [i]
        j = i - 1
        while j >= 0 and  key > arr[j]:
            arr [j + 1] = arr[j]
            j = j - 1 
        arr [j + 1] = key
### **Linear Search**

Pseudo Code
    
    LinearSearch(A, v)
        for i = 1 to A.length
            if A[i] == v
            return i
        return NIL

Code in python 

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

**The time complexity of the above algorithm is O(n).**





