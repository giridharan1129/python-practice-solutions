#search a character and find the number of times it occured

a=input('enter string :')
b=input('enter search character :')
c=0
for i in a:
    if i==b:
        c=c+1

z='{} was found {} times'
print(z.format(b,c))        