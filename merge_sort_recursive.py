def sort(arr, lo=0, hi=None):
    if hi is None: hi = len(arr)
    if lo >= hi: return []
    if lo+1 == hi: return [arr[lo]]
    mid = (lo+hi)//2
    larr = sort(arr, lo, mid)
    rarr = sort(arr, mid, hi)
    li, ri, ln, rn = 0, 0, mid-lo, hi-mid
    marr = [None]*(ln+rn)
    while li<ln and ri<rn:
        if larr[li] <= rarr[ri]:
            marr[li+ri] = larr[li]
            li += 1
        else:
            marr[li+ri] = rarr[ri]
            ri += 1
    while li<ln:
        marr[li+ri] = larr[li]
        li += 1
    while ri<rn:
        marr[li+ri] = rarr[ri]
        ri += 1
    return marr

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('before', arr)
    arr = sort(arr)
    print('after', arr)
