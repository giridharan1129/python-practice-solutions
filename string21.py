# Python program to remove the characters which have odd index values of a given string
a=input('enter string :')
s=''
for i in range(0,len(a)):
    if i%2!=0:
        s+=a[i]
print(s)