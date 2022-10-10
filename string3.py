#to count number of vowels in a string
# def vowels(a):
a=input('enter string :')
a=a.lower()
count=0
for i in a:
    if i in ['a','e','i','o','u']:
        count = count+1 
print('number of vowels:',count)      



# print('number of vowels :',count)
