#Find Maximum & Minimum Element In list - Python Interview Question
arr=[12,23,43,12,11,18,76,99,56,43]

def maximum(arr):
    max=arr[0]
    for i in range(len(arr)) :
        if arr[i]>max:
            max=arr[i]
    print('maximum is :',max)   

maximum(arr)

def minimum(arr):
    min=arr[0]
    for i in range(len(arr)) :
        if arr[i]<min:
            min=arr[i]
    print('minimum is :',min)  

minimum(arr)
