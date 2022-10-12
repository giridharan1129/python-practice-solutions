#WAVE ARRAY - DS & ALGO WITH PYTHON CODE -AMAZON,GOOGLE,ADOBE INTERVIEW QUESTION
arr=[1,8,3,5,1,8,65,90]
def wave(arr):
    for i in range(0,len(arr),2):
        if arr[i+1]>arr[i]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
        if i>0 and arr[i-1]>arr[i]:
            arr[i],arr[i-1]=arr[i-1],arr[i]
    print(arr)

wave(arr)    