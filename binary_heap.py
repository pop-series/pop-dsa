def _parent(x):
    return (x-1)//2

def _lchild(x):
    return 2*x+1

def _rchild(x):
    return 2*x+2

def _heapify_down(items, n, last_pidx, idx):
    while idx <= last_pidx:
        target = idx
        lidx, ridx = _lchild(idx), _rchild(idx)
        if lidx < n and items[lidx] < items[target]:
            target = lidx
        if ridx < n and items[ridx] < items[target]:
            target = ridx
        if target != idx:
            items[idx], items[target] = items[target], items[idx]
            idx = target
        else:
            return

def heapify(items):
    n = len(items)
    last_pidx = _parent(n-1)
    for idx in range(last_pidx, -1, -1):
        _heapify_down(items, n, last_pidx, idx)

def heappush(heap, item):
    heap.append(item)
    idx = len(heap)-1
    pidx = _parent(idx)
    while idx > 0 and heap[idx] < heap[pidx]:
        heap[idx], heap[pidx] = heap[pidx], heap[idx]
        idx = pidx
        pidx = _parent(idx)

def heappop(heap):
    if not heap:
        return None
    n = len(heap)
    if n == 1:
        return heap.pop()
    item = heap[0]
    heap[0] = heap.pop()
    last_pidx = _parent(n-2)
    _heapify_down(heap, n-1, last_pidx, 0)
    return item        

def heappushpop(heap, item):
    if not heap or item < heap[0]:
        return item
    heap[0], item = item, heap[0]
    n = len(heap)
    last_pidx = _parent(n-1)
    _heapify_down(heap, n, last_pidx, 0)
    return item

def heapreplace(heap, item):
    if not heap:
        heap.append(item)
        return None
    n = len(heap)
    last_pidx = _parent(n-1)
    heap[0], item = item, heap[0]
    _heapify_down(heap, n, last_pidx, 0)
    return item

def heapmerge(heap1, heap2):
    heap = heap1 + heap2
    heapify(heap)
    return heap
