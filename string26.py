#Python Program Change A Given String To A New String Where First And Last Chars Have Been Exchanged
def change_char(str):
    return str[-1:]+str[1:-1]+str[:1]

str=input('enter string :')
print(change_char(str))
