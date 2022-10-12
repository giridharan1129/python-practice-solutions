#Maximum Sum SubArray (Kadane's algorithm) With Algorithm & Python Code
arr=[-1,4,-7,-8,7,4,3,2,-3,0,9,6,5]

def maxsub(arr):
    csum=0
    max=arr[0]
    poi=0
    s=0
    e=0
    for i in range(0,len(arr)):
        csum+=arr[i]
        if max<csum:
            max=csum
            s=poi
            e=i
        if csum<0:
            csum=0
            poi=i+1
    print('maximum sum :',max)
    print('start index :',s)
    print('end index :',e)

maxsub(arr)


