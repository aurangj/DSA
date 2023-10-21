arr = [ 16, 17, 4,3,5,2]
n_arr= [ 16, 17, 4,3,5,2,-1]
n_arr[len(arr)] = -1
print(n_arr)
k = 0
for i in range((len(arr)-1),0,-1):
    if arr[i] > n_arr[i+1]:
        n_arr[i] = arr[i]
    else:
        n_arr[i] = n_arr[i+1]
print(n_arr)




