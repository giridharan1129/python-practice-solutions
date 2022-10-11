#Input a sentence from user and print the longest word in capital
a=input('enter string :')
b=a.split()
largest=b[0]
for i in range(0,len(b)):
    if len(largest)<len(b[i]):
        largest=b[i]
print('largest word is :',largest.upper())   
