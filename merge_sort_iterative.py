def _largest_window(x):
    if not(x & (x-1)):
        return x
    return 1 << (x.bit_length()+1)

def sort(arr):
    n = len(arr)
    W = _largest_window(n)
    window = 2
    while window <= W:
        for idx in range(0, n, window):
            mid = (idx+idx+window)//2
            mi, li, ri, ln, rn = 0, idx, mid, mid, min(idx+window, n)
            marr = [None]*window
            while li<ln and ri<rn:
                if arr[li] <= arr[ri]:
                    marr[mi] = arr[li]
                    mi, li = mi+1, li+1
                else:
                    marr[mi] = arr[ri]
                    mi, ri = mi+1, ri+1
            while li<ln:
                marr[mi] = arr[li]
                mi, li = mi+1, li+1
            while ri<rn:
                marr[mi] = arr[ri]
                mi, ri = mi+1, ri+1
            for ai in range(idx, rn):
                arr[ai] = marr[ai-idx]
        window *= 2

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('before', arr)
    sort(arr)
    print('after', arr)
