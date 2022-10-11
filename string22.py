#Python Program To Check A String Is Palindrome Or Not Using Recursion
from operator import truediv


def palindrome(string):
    if len(string)<=1:
        return 'palindrome'
    if string[0]==string[len(string)-1]:
        return palindrome(string[1:len(string)-1])
    else:
        return 'Not palindrome'

string=input('enter string :')
print(palindrome(string))
