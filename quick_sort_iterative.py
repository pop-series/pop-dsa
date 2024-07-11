from collections import deque
import random

def _swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def sort(arr, lo=0, hi=None, pivotFunc=None):
    if hi is None: hi = len(arr)
    if pivotFunc is None: pivotFunc = lambda a, b: random.randint(a, b-1)
    buf = deque([(lo, hi)])
    while buf:
        tlo, thi = buf.popleft()
        if tlo == thi: continue
        pivot = pivotFunc(tlo, thi)
        _swap(arr, pivot, thi-1)
        pval = arr[thi-1]
        mi = tlo
        for idx in range(tlo, thi-1):
            if arr[idx] < pval:
                _swap(arr, idx, mi)
                mi += 1
        _swap(arr, mi, thi-1)
        buf.append((tlo, mi))
        buf.append((mi+1, thi))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('before', arr)
    sort(arr)
    print('after', arr)
