# Move all negative elements to end
# Given an unsorted array arr[] of size N having both negative and positive integers.
# The task is place all negative element at the end of array without changing the order of positive element and negative element.
arr= [1, -1, 3, 2, -7, -5, 11, 6]
def segregateElements(arr):
        b=[]
        d=[]
        for i in range(len(arr)):
            if arr[i]<0:
                b.append(arr[i])
            else:
                d.append(arr[i])
        c=d+b
        return c

print(segregateElements(arr))