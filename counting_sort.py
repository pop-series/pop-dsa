def sort(arr):
    M = max(arr)
    counter = [0]*(M+1)
    for val in arr:
        counter[val] += 1
    for idx in range(1, M+1):
        counter[idx] += counter[idx-1]
    N = len(arr)
    opt = [None]*N
    for idx in range(N-1, -1, -1):
        val = arr[idx]
        opt[counter[val]-1] = val
        counter[val] -= 1
    return opt

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('before', arr)
    print('after', sort(arr))
