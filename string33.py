#Write a Python program to remove the numeric digits from string Python
a=input('enter string :')
b=''
for i in a:
    if ord(i) in range(97,123) or i.isspace():
        b+=i
print(b)

# for i in a:
#     if i.isdigit():
#         continue
#     else:
#         b+=i
# print(b)
