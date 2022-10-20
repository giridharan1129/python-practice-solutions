str=input('enter string :')

def tolower(str):
    a=''
    for i in str:
        if i.isupper():
            a+=i.lower()
        else:
            a+=i
    return a    


print(tolower(str))