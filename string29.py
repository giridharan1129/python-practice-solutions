#Remove All Duplicates From A Given String In Python
a=input('enter string :')
b=''
for i in a:
    if i not in b:
        b+=i
print(b)

