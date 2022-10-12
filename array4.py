#Remove Duplicates from Sorted Array (With Algorithm & Python Code)
arr=[1,1,2,3,3,4,4,5,5,5,5,6,6,7,8,9]
n=len(arr)
if n==0 or n==1:
    print(arr)
temp=[0]*n
pivot=0
for lasto in range(0,n-1):
    if arr[lasto]!=arr[lasto+1]:
        temp[pivot]=arr[lasto]
        pivot+=1
temp[pivot]=arr[n-1]
print(temp[0:pivot+1])