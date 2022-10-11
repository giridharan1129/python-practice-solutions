# 10: Python program to check if two strings are anagram or not
a=input('enter string :')
print(sorted(a))
b=input('enter string :')
print(sorted(b))
if sorted(a)==sorted(b):
    print("they are anagram")
else:
    print('Not anagram')