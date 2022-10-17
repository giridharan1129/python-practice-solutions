n=int(input('enter number :'))
def number_units(n):
    b=1
    d=[]
    while n>0:
        a=n%10
        c=a*(b)
        n=n//10
        b=b*10
        if c>0:
            d.append(c)
    print(d[::-1])
    
    
number_units(n)

# n=int(input('enter number :'))

# def numrev(n):
#     c=0
#     while n>0:
#         a=n%10
#         c=a+(c*10)
#         n=n//10
#     return c


# print(numrev(n))