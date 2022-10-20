str=input('enter string :')
def reverse_str(str):
    a=[]
    for i in range(len(str)):
        a.append(str[i])    
    left,right=0,len(a)-1
    while left<=right:
        a[left],a[right]=a[right],a[left]
        left,right=left+1,right-1
    return ''.join(a)

print(reverse_str(str))