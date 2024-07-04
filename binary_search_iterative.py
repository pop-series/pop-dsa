def search_left(arr, val, lo=0, hi=None):
    if hi is None: hi = len(arr)
    while lo != hi:
        mid = (lo+hi)//2
        if arr[mid] >= val:
            hi = mid
        else:
            lo = mid+1
    return lo

def search_right(arr, val, lo=0, hi=None):
    if hi is None: hi = len(arr)

    while lo != hi:
        mid = (lo+hi)//2
        if arr[mid] > val:
            hi = mid
        else:
            lo = mid+1
    return lo

def insort_left(arr, val, lo=0, hi=None):
    idx = search_left(arr, val, lo, hi)
    arr.insert(idx, val)

def insort_right(arr, val, lo=0, hi=None):
    idx = search_right(arr, val, lo, hi)
    arr.insert(idx, val)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    val = int(input().strip())

    left_idx = search_left(arr, val)
    print("left:", left_idx)

    right_idx = search_right(arr, val)
    print("right:", right_idx)
