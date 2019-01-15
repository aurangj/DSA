
# only required to keep  array n size of right max.
# left max wil be calculated as  iterate through it.

def area(arr):
    sum = 0
    arr_rightmax = []
    length = len(arr) - 1
    arr_rightmax.append(arr[length])
    for i,value in reversed(list(enumerate(arr))):

        if i == length:
            continue
        arr_rightmax.append(max(arr[i], arr_rightmax[-1]))

    arr_rightmax.reverse()
    left_max = arr[0]

    for i, value in enumerate(arr, start=0):
        if arr[i] > left_max:
            left_max = arr[i]
        sum = sum + (min(left_max,arr_rightmax[i]) - arr[i])

    return sum


if __name__ == '__main__':
    #arr = [4,2,0,6,2,3]
    arr = [6,2,0,1,2,6]
    print(area(arr))

