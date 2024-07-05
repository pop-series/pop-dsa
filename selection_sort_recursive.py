def sort(arr, start=0, n=None):
    if n is None: n = len(arr)
    if start == n:
        return
    min_idx = start
    for idx in range(start+1, n):
        if arr[idx] < arr[min_idx]:
            min_idx = idx
    arr[start], arr[min_idx] = arr[min_idx], arr[start]
    sort(arr, start+1, n)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('before', arr)
    sort(arr)
    print('after', arr)
