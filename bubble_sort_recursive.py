def sort(arr, end=None):
    if end is None: end = len(arr)-1
    swap = False
    for idx in range(end):
        if arr[idx] > arr[idx+1]:
            arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
            swap = True
    if swap:
        sort(arr, end-1)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('before', arr)
    sort(arr)
    print('after', arr)
