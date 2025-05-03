def selectionsort(arr):
  for i in range(len(arr)):
    min_x = i

    for item in range(i+1,len(arr)):
      if arr[item] < arr[min_x]:
        min_x = item


arr = [12,45,13,2,6,1]
selectionsort(arr)

print(arr)
    
