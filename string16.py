#Inputs A String With Multiple Words And Then Capitalises The First Letter Of Each Word
a=input('enter string :')
l=[]
temp=''
f=''
for i in a:
    if i!=' ':
        temp=temp+i
    else:
        l.append(temp)
        temp=''
l.append(temp)
for i in range(0,len(l)):
    temp=l[i]
    f=f +' '+ temp.capitalize()
print(f)