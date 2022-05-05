import time
import random

def shellsort(arr):
    N = len(arr)
    h = N // 2
    while h > 0:
        for i in range(h, N):
            temp = arr[i]
            j = i - h
            while j >= 0 and arr[j] > temp:
                arr[j + h] = arr[j]
                j -= h
            arr[j + h] = temp
        h //= 2
 
 
for i in range(5,22,1):
   
    arr=[]  
    for i in range(2**i,0,-1):
        arr.append(i)
  
    start = time.time()
    shellsort(arr)
    print(time.time()-start)
