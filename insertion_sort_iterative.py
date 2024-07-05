def sort(arr):
    n = len(arr)
    for idx in range(1, n):
        val, target_idx = arr[idx], idx-1
        while target_idx >= 0 and arr[target_idx] > val:
            arr[target_idx+1] = arr[target_idx]
            target_idx -= 1
        arr[target_idx+1] = val


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('before', arr)
    sort(arr)
    print('after', arr)
