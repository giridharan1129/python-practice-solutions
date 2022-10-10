#to reverse a string

a= input('enter string :')
s=""
b=0
for i in a:
    b=b+1
for i in range(1,b+1):
    s= s + a[b-i]
print(s)        