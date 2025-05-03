def bubblesort(arr):
    for iter in range(len(arr)):
        for i in range(0,len(arr) - 1 - iter):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] =arr[i+1],arr[i]

    
arr = [12,13,51,26,11,14]
bubblesort(arr)
print(arr)
