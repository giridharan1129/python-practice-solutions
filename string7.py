#palindrome of string

a= input('enter string :')
def string(a):
    for i in range(0,len(a)):
        i2 = len(a)-i-1
        if a[i]!=a[i2]:
            return 'not palindrome'   
    return 'Palindrome'

print(string(a))