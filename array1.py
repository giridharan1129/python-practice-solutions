#reverse of a list
l=[1,2,3,4]
l2=[]
for i in range(len(l)-1,-1,-1):
    l2.append(l[i])
print(l2)