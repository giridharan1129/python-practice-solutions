#convert a string to list without split function
a= input('enter string :')
l=[]
temp=''
for i in a:
    if i== ' ':
        l.append(temp)
        temp=''
    else:
        temp=temp+i
l.append(temp)
print(l)
