# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
str=input('enter roman number :')
def roman_to_int(str):
    current=0
    previous=0
    sum=0
    for i in range(len(str)):
        current=dict[str[i]]
        if current>previous:
            sum+=current-2*previous
        else:
            sum+=current
        previous=current
    return sum

print(roman_to_int(str))
        
    