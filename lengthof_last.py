#length of last word
str=(input('enter string :'))

def length_of_lastword(str):
    length=0
    i=len(str)
    while i>0:
        i-=1
        if str[i]!=' ':
            length+=1
        elif length >0:
            return length
    return length

print(length_of_lastword(str))