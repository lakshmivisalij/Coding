def bubbleSort(arr):
    n  = len(arr)
    
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr
    
arr = [1, 2 , 3 , 4, 6 , 5, 7, 9, 8, 8 ]

ar = bubbleSort(arr)
print(ar)