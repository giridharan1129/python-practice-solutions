#Python Program To Remove All Duplicates Words From A Given Sentence
a=input('enter a sentence :')
a=a.split()
b=[]
for i in a:
    if i not in b:
        b.append(i)
a=''
for i in b:
    a+=i+" "

print(a)
