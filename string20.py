#Python program to prints a string that capitalizes every alternate letter in the string
a=input('enter string :')
s=''
for i in range(0,len(a)):
    if i%2==0:
        s+=a[i].upper()
    else:
        s+=a[i].lower()
print(s)

