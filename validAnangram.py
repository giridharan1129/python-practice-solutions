inp1=input('enter string 1 :')
inp2=input('enter string 2 :')

dict1={}
dict2={}
count1=0
count2=0
for i in range(97,123):
        count=0
        j=chr(i)
        for l,m in inp1,inp2:
            if j==l:
                count1+=1
            if j==m:
                count2+=1
        if count>0:
            dict1[j]=count1
            dict2[j]=count2
# dict2={}
# count=0
# for i in range(97,123):
#         count=0
#         j=chr(i)
#         for l in inp2:
#             if j==l:
#                 count+=1
#         if count>0:
#             dict2[j]=count
            
if(dict1==dict2):
    print('they are anagrams')
else:
    print('they are not anagrams')