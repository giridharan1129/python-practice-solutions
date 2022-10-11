#Python Program to Count the occurrences of each word in a given sentence
a=input('enter a sentence :')
a=a.split()
i=0
while i<len(a):
    count=0
    for j in a:
        if a[i]==j:
            count+=1
    print(a[i], 'is present',count,'times')
    i+=1