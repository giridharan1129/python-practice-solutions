# Count substrings made up of a single distinct character
# Input: str = “geeksforgeeks”
# Output: 15
# Explanation: All substrings made up of a single distinct character are {“g”, “e”, “ee”, “e”, “k”, “s”, “f”, “o”, “r”, “g”, “e”, “ee”, “e”, “k”, “s”}.
str=input('enter string :')
def distinctSubstring(str):
    ans=0
    subs=0
    pre=''
    for i in str:
        if i==pre:
            subs+=1
        else:
            subs=1
            pre=i
        ans+=subs
    return ans


print(distinctSubstring(str))
    