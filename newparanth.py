#valid brackets
def are_pairs(open,close):
    if open=='['and close==']':
        return True
    if open=='('and close==')':
        return True
    if open=='{'and close=='}':
        return True
    return False
str=input('enter string with brackets :')  
def is_valid_brackets(str):
    arr=[]  
    for i in range(len(str)):
        if str[i]=='[' or str[i]=='{' or str[i]=='(':
            arr.append(str[i])
        elif (str[i]==']' or str[i]=='}' or str[i]==')') and len(arr)!=0 :
            if are_pairs(arr[-1],str[i]) :
                arr.pop()
            else:
                return 'not valid'
        elif (str[i]==']' or str[i]=='}' or str[i]==')') and len(arr)==0 :
            return 'Not valid'
    if len(arr)==0:
        return 'valid brackets'
    else:
        return'not valid brackets'    
        
print(is_valid_brackets(str))



        