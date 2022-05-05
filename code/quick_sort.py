import time
import random
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quicksort(lesser_arr) + equal_arr + quicksort(greater_arr)

for i in range(5,21,1):
   
    arr=[]  
    for i in range(2**i,0,-1):
        arr.append(i)
    start = time.time()
    quicksort(arr)
    print(time.time()-start)