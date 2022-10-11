#Removing nth Character From A String In Python Program
a=input('enter string :')
n=int(input('position to remove :'))
c=''
for i in range(len(a)):
    if i!=n:
        c+=a[i]
print(c)        
