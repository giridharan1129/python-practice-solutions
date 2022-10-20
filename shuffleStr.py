str=input('enter string :')
ind=[0,5,1,6,2,4,3]
def shuffle_str(str,ind):
    fin_str =[0]*len(ind)
    for i in range(len(ind)):
        fin_str[ind[i]]=str[i]
    return ''.join(fin_str)     
        
print(shuffle_str(str,ind))