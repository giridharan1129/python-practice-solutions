#Inputs A String With Multiple Words And Then Capitalises The First Letter Of Each Word
a=input('enter string :')
a=' '+a
s=''
c=0
for i in range(0,len(a)):
    if a[i]==' ':
        s+=' '+a[i+1].upper()
        c=i+2
    else:
        s+=a[c]
        c=c+1
    if c==len(a):
        break
print(s)