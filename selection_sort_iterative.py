def sort(arr):
    n = len(arr)
    for start in range(n):
        min_idx = start
        for idx in range(start+1, n):
            if arr[idx] < arr[min_idx]:
                min_idx = idx
        arr[start], arr[min_idx] = arr[min_idx], arr[start]


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('before', arr)
    sort(arr)
    print('after', arr)
