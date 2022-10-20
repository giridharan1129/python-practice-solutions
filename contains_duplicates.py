#contains duplicates-Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.(leetcode-217) 
from re import A


array=[1,2,3,4,2,3]
def containsDuplicates(array):
    A=set()
    for i in array:
        if i in A:
            return True
        A.add(i)
    return False
        
print(containsDuplicates(array))        