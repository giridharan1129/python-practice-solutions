haystack=input('enter haystack string :')
needle=input('enter needle string :')

#1
def strstr(haystack,needle):
    if needle=='':
        return 0
    for i in range(len(haystack)+1-len(needle)):
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1


print(strstr(haystack,needle))


#2
def strstr(haystack,needle):
    if needle=='':
        return 0
    
    for i in range(len(haystack)+1-len(needle)):
        for j in range(len(needle)):
            if haystack[i+j]!=needle[j]:
                break
            if j==len(needle)-1:
                return i
    return -1

print(strstr(haystack,needle))




    
# def strstr(haystack,needle):
#     i=0
#     j=0
#     while i<len(haystack):
#         if haystack[i]==needle[j]:
#             i+=1
#             j+=1
#             if haystack[i]==needle[j]:
#                 return i-1
#             else:
#                 i+=1
#                 j=0
#         else:
#             i+=1
#     return -1    
        
        
# print(strstr(haystack,needle))