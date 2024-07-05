def sort(arr, start=1, n=None):
    if n is None: n = len(arr)
    if start == n:
        return
    val, target_idx = arr[start], start-1
    while target_idx >= 0 and arr[target_idx] > val:
        arr[target_idx+1] = arr[target_idx]
        target_idx -= 1
    arr[target_idx+1] = val
    sort(arr, start+1, n)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('before', arr)
    sort(arr)
    print('after', arr)
