"""Searching for a specific target element ,once the element is found that element is brought to the end of the array"""
def modification_array(ar, tar):
    i = j = len(ar)-1
    for i in range(i, -1, -1): #(start,i = ar-1, stop = i < -1 , step = i=i-1)
        if ar[i] == tar:
            ar[i], ar[j] = ar[j], ar[i]
            j -= 1


    return ar


arr = [6,1,6,8,10,4,15,6,3,9,6]
target = 6
res = modification_array(arr,target)
print(res)