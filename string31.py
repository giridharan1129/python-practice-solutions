#Removing nth Character From A String In Python Program
a=str(input('enter string :'))
b=int(input('position to remove :'))
def removepos(str):
    return a[0:b]+a[b+1:len(a)+1]

print(removepos(a))

