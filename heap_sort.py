def _heapify_down(items, n, last_pidx, idx):
    while idx <= last_pidx:
        tidx, lidx, ridx = idx, idx*2+1, idx*2+2
        if lidx < n and items[lidx] > items[tidx]:
            tidx = lidx
        if ridx < n and items[ridx] > items[tidx]:
            tidx = ridx
        if tidx != idx:
            items[idx], items[tidx] = items[tidx], items[idx]
            idx = tidx
        else:
            return

_parent = lambda idx: (idx-1)//2

def sort(arr):
    n = len(arr)
    last_pidx = _parent(n-1)
    for idx in range(last_pidx, -1, -1):
        _heapify_down(arr, n, last_pidx, idx)
    for idx in range(n-1, 0, -1):
        arr[0], arr[idx] = arr[idx], arr[0]
        _heapify_down(arr, idx, _parent(idx-2), 0)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('before', arr)
    sort(arr)
    print('after', arr)
