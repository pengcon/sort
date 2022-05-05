import time
import random


def selectionSort(array, size):
   
    for step in range(size):
        min = step

        for i in range(step + 1, size):
         
            
            if array[i] < array[min]:
                min = i
         
     
        (array[step], array[min]) = (array[min], array[step])




for i in range(5,22,1):
    start = time.time()
    arr=[]  
    for i in range(1,2**i):
        arr.append(i)
    size = len(arr)

    start = time.time()
    selectionSort(arr, size)
    print(time.time()-start)



