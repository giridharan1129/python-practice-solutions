#check if a string is a palindrome or not
a= input('enter string :')  
s=0
sa=""
for i in a:
    s=s+1
for j in range(1,s+1):
    sa= sa + a[s-j]
if sa==a:
    print(a,' is palindrome')
else:
    print(a,' is not palindrome')

