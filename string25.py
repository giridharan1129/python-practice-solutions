#Write a Python program to remove all extra blank spaces from given string.
a=input('enter string :')
b=''
c=a.split()
for i in range(0,len(c)):
    b+=' '+c[i]
print(a)
print(b)