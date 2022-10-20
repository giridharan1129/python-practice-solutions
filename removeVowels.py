str=input('enter string :')
def remove_vowels(str):
    s=''
    vowels='aeiouAEIOU'
    for i in str:
        if i not in vowels:
            s+=i
    return s

print(remove_vowels(str))
