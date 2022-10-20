str=input('enter sentence :')
def sentence_palindrome(str):
    a=""
    for i in str:
        if i.isalpha():
            a+=i.lower() 
    print(a) 
    left=0
    right=len(a)-1 
    while left<=right:
        if a[left]!=a[right]:
            return 'not palindrome'
        left+=1
        right-=1
    return 'palindrome'
        
            

print(sentence_palindrome(str))