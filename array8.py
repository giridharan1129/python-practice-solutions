# Arrays - Odd Even Subsequences
arr=[1,6,3,2,4,1,5,7,9,0]
b=[arr[0]]
def oddeven_subseq(arr):
    for i in arr[1:]:
        if i%2 != b[-1]%2:
            b.append(i)
    return b

print(oddeven_subseq(arr))

            


