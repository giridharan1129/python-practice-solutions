# An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
# Given an array arr[] of size N, Return the index of any one of its peak elements.
# Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0. 
def peakElement(arr, n):
        # Code here
        if n==1:
            return 0
        if(arr[0]>=arr[1]):
            return 0
        if (arr[n-1]>=arr[n-2]):
            return n-1 
        
        for i in range(1,n-1):
            if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
                return i

n=8
arr=[1,3,5,7,9,2,10,4]
print(peakElement(arr, n))