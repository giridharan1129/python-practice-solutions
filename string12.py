#to print initials of name with surname i/p:mohandas karamchand gandhi o/p:M.K.Gandhi

a=input('enter string :')
b=a.split()
n=""
for i in range(len(b)-1):
    s= b[i]
    n=n+s[i].capitalize() + '.'
n=n+b[-1].capitalize()
print(n)    



