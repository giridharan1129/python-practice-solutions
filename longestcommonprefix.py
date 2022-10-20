str=['flow','flight','flu']
def longest_prefix(str):
    if len(str)==0:
        return ''
    minlength=len(str[0])
    for i in range(len(str)):
        minlength=min(len(str[i]),minlength)
    lcp=''
    i=0
    while i<minlength:
        char=str[0][i]
        for j in range(1,len(str)):
            if str[j][i]!=char:
                return lcp
        lcp+=char
        i+=1
    return lcp
            
    

print(longest_prefix(str))