# Q3) WAP to reverse every word of string in proper manner.
# I/O: this is my book
# O/P: siht si ym koob

t=input('enter string :')
a=t.split(' ')
for w in a:
    print(w[::-1], end=" ")
