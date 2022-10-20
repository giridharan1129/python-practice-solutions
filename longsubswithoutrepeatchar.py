#to return maximum length of a substring without repeating characters

str=input('enter string :')
def longest_subs(str):
    if len(str)==0:
        return 0
    map={}
    start=0
    max_length=0
    for i in range(len(str)):
        if str[i] in map and start<=map[str[i]]:
            start=map[str[i]] +1
        else:
            max_length=max(max_length,i-start+1)
            print(max_length)
        map[str[i]]=i
        print(str[start:(max_length+2)])
            
print(longest_subs(str))        
        