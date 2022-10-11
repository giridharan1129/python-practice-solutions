#Python Program to Find smallest and largest word in a given string
a=input('enter string :')
b=a.split()
largest=smallest=b[0]
for i in range(0,len(b)):
    if len(largest)<len(b[i]):
        largest=b[i]
        
    if len(smallest)>len(b[i]):
        smallest=b[i]

print(smallest,'is the smallest word')
print(largest,'is the largest word')
