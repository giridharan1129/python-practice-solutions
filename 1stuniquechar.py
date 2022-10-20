str=input('enter string :')

#2
def first_unique_char(str):
    dict={}
    count=0
    for i in range(97,123):
        count=0
        j=chr(i)
        for l in str:
            if j==l:
                count+=1
        if count>0:
            dict[j]=count
    for i in range(len(str)):
        if dict[str[i]]==1:
            return i
    return -1            
           
print(first_unique_char(str))

#1
def firstUniqChar(str):
 
      frequency = {}
      for i in str:
         if i not in frequency:
            frequency[i] = 1
         else:
            frequency[i] +=1
      for i in range(len(str)):
         if frequency[str[i]] == 1:
            return i
      return -1


print(firstUniqChar(str))