arr = [4, 3, 7, 8, 6, 2, 1]
arr = [1, 4, 2, 3]
print(arr)
for k in range(len(arr)-1):
    if (k+1) % 2 != 0:
        if arr[k] > arr[k+1]:
            temp = arr[k]
            arr[k] = arr[k+1]
            arr[k+1] = temp
    else:
        if arr[k] < arr[k+1]:
            temp = arr[k]
            arr[k] = arr[k+1]
            arr[k+1] = temp
print(arr)