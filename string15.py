#Write A Python Program To Compute Sum Of Digits in A Given String
a= input('enter string :')
digit=''
sums=0
for i in range(0,len(a)):
    if (a[i].isdigit()):
        digit=digit+a[i]
        sums=sums+int(a[i])
if sums==0:
    print('no digit in string')
else:
    print('sum of digits :',sums)
    print('o string :',a)
    print('digits',digit)