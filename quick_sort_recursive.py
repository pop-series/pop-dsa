import random

def _swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def sort(arr, lo=0, hi=None, pivotFunc=None):
    if hi is None: hi = len(arr)
    if lo == hi: return
    if pivotFunc is None: pivotFunc = lambda a, b: random.randint(a, b-1)
    pivot = pivotFunc(lo, hi)
    _swap(arr, pivot, hi-1)
    pval = arr[hi-1]
    mi = lo
    for idx in range(lo, hi-1):
        if arr[idx] < pval:
            _swap(arr, idx, mi)
            mi += 1
    _swap(arr, mi, hi-1)
    sort(arr, lo, mi, pivotFunc)
    sort(arr, mi+1, hi, pivotFunc)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('before', arr)
    sort(arr)
    print('after', arr)
