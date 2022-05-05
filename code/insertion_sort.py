import time
import random





def insertionSort(arr):

    for i in range(1, len(arr)):
 
        key = arr[i]
 
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
 
for i in range(5,22,1):

    arr=[]  
    for i in range(1,2**i):
        arr.append(i)
    random.shuffle(arr)
    start = time.time()
    insertionSort(arr)
    print(time.time()-start)


