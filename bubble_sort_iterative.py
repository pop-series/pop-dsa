def sort(arr):
    n = len(arr)
    for end in range(n-1, 0, -1):
        swap = False
        for idx in range(end):
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
                swap = True
        if not swap:
            return

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('before', arr)
    sort(arr)
    print('after', arr)
