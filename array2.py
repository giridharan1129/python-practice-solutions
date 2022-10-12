#Find out pairs with given sum value in an array
arr=[1,2,3,4,5,6,7,8,9,0]
num=int(input('enter sum value :'))

def arraysum(arr,num):
    arr.sort()
    left=0
    right=len(arr)-1
    while left<=right:
        if arr[left]+arr[right]<num:
            left+=1
        elif arr[left]+arr[right]>num:
            right-=1
        elif arr[left]+arr[right]==num:
            print('the pairs are :',arr[left],arr[right])
            left+=1
            right-=1
 
arraysum(arr,num) 

# n=int(input('enter sum value :'))
# for i in l:
#     for j in l:
#         if i+j==n:
#             print(i,j)