# Welcome to the my Learning Path of Python

Hi devs here **Masha**!

This repository it's very personal and important, because I'm in my last semester of the University and I set a personal goal.

 **Be a Python Developer to get in a big tech company !!!**


- [Welcome to the my Learning Path of Python](#welcome-to-the-my-learning-path-of-python)
  - [**Personal Experience**](#personal-experience)
    - [**Style Guide (PEP8)**](#style-guide-pep8)
    - [**Udacity Python Course**](#udacity-python-course)
      - [Arithmetic Operators](#arithmetic-operators)
      - [Varibles](#varibles)
    - [**Algorithms study**](#algorithms-study)
      - [**Insertion Sort**](#insertion-sort)
      - [**Code in Python (Example)**](#code-in-python-example)
      - [**Linear Search**](#linear-search)
      - [**SelectionSort**](#selectionsort)
## **Personal Experience**

Actually right now I'm a Application developer at IBM, working with API's in **Spring Boot(JAVA)** also working with a little bit of **Scala** and **Spark**

### **Style Guide (PEP8)**

In this repositorie or course, I´ll using the guide style for python **PEP8** so the following code will be in this format.
[PEP8 Guide Link](https://www.python.org/dev/peps/pep-0008/)

### **Udacity Python Course**

#### Arithmetic Operators

- Addition +
- Subtraction -
- Multiplication *
- Division /
- Mod %
- Exponentiation **
- Divides and rounds down to the nearest integer //

#### Varibles 

- Variables are used to hold information about something that you will use later


    a = 123

- You can have **Multiple** assigment using 

    x,y,z = 2, 3, 5

- The variable has to be descripted and useful for you and the other developers

**The pythonic way to name varialbles is to use all lowercase letters and underscores to separte words**

    Example: my_long

- Assignment Operators
  - Example is x = 2 -> x = 2
  - += x+=2 -> x = x + 2
  - -= x-=2 -> x = x - 2

### **Algorithms study**

#### **Insertion Sort** 
This algorithm work to sort an array of numbers this is working with small quantity of numbers.
- **Time complexity it´s of: O(n^2)** 
- **Auxiliary Space: O(1)**

#### **Code in Python (Example)**
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
#### **Linear Search**

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

#### **SelectionSort**

Pseudo Code

    n = A.length
    for i = 1 to n - 1
        minIndex = i
        for j = i + 1 to n
            if A[j] < A[minIndex]
                minIndex = j
        swap(A[i], A[minIndex])

Code in Python

    import sys
    print ("Answer Θ(n^3")

    A = [64,25,12,22,11]

    for i in range(len(A)):
        
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
                
        A[i], A[min_idx] = A[min_idx], A[i]
    print ("Sorted array is")
    for i in range(len(A)):
        print("%d" %A[i])





