str=input('enter string :')
def balancedPartition(str):
    if len(str)==0:
        return 0
    r=0
    l=0
    ans=0
    for i in str:
        if i=='R':
            r+=1
        elif i=='L':
            l+=1
        if r==l:
            ans+=1
            r=0
            l=0
    return ans


print(balancedPartition(str))            