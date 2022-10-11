#Python Program To convert a lowercase character to uppercase and uppercase to lowercase
a=input('enter string :')
s=''
for i in a:
    if ord(i) in range(65,91):
        s+= i.lower()
    else:
        s+= i.upper() 
print(s)
s