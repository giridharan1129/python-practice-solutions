#FIND MISSING NUMBER IN AN ARRAY IN PYTHON
arr=[1,2,3,4,6,7,8,9]
def missing_num(arr):
    sum1 = (arr[-1]*(arr[-1]+1))//2
    s=0
    for i in range(len(arr)):
        s+=arr[i]
    print(sum1-s)

missing_num(arr)

def missing_num_xor(arr):
    n=len(arr)
    xor=arr[0]
    for i in range(1,n):
        xor=xor^arr[i]
    x2=0
    for i in range(1,n+2):
        x2=x2^i
    print(xor^x2)

missing_num_xor(arr)


