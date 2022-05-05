import time
import random



def bubbleSort(arr):
    n = len(arr)
 
    
    for i in range(n-1):

 
      
        for j in range(0, n-i-1):
 
           
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 

for i in range(5,22,1):
    start = time.time()
    arr=[]  
    for i in range(2**i,0,-1):
        arr.append(i)
    start = time.time()
    bubbleSort(arr)
    print(time.time()-start)


 


print(time.time()-start)