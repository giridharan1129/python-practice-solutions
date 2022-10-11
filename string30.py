#Python Program To Remove Special Characters From String
a= input('enter string :')
a=a.lower()
b=''
for i in a:
    if ord(i) in range(97,123):
        b+=i
print(b)