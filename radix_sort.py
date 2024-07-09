def counting_sort(arr, key=None, M=None):
    if key is None: key = lambda x: x
    if M is None: M = max(map(key, arr))
    counter = [0]*(M+1)
    for val in arr:
        counter[key(val)] += 1
    for idx in range(1, M+1):
        counter[idx] += counter[idx-1]
    n = len(arr)
    opt = [None]*n
    for idx in range(n-1, -1, -1):
        val = arr[idx]
        k = key(val)
        opt[counter[k]-1] = val
        counter[k] -= 1
    for idx in range(n):
        arr[idx] = opt[idx]

def sort(arr):
    amax, fact = max(arr), 1
    while amax // fact >= 1:
        counting_sort(arr, lambda x: int((x//fact)%10), 9)
        fact *= 10


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('before', arr)
    sort(arr)
    print('after', arr)
