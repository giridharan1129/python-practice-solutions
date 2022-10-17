array=[1,2,3,4,5]
def missing_num(array):
    alength = array[-1]-array[0]+1
    if alength==len(array):
        return 'no missing number'
    sum=0
    sumo=((array[-1]-array[0]+1)/2)*(array[0]+array[-1])
    print(sumo)
    for i in range(len(array)):
        sum+=int(array[i])
    missing_num = (sumo-sum)
    return missing_num
        
print(missing_num(array))        
        
    