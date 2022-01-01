import sys

#Express the function n^3/1000 - 100n^2 +3n in therms of Θ-notation
print ("Answer Θ(n^3")

A = [64,25,12,22,11]

for i in range(len(A)):
    
# Find the minimum element in remaining
# unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
            
    # Swap the found minimum element with
    # the first element       
    A[i], A[min_idx] = A[min_idx], A[i]
print ("Sorted array is")
for i in range(len(A)):
    print("%d" %A[i])