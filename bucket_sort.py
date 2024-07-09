def sort(arr):
    buckets = [[] for _ in range(10)]
    for val in arr:
        buckets[int(val*10)].append(val)
    idx = 0
    for bucket in buckets:
        bucket.sort() # any stable sort
        for val in bucket:
            arr[idx] = val
            idx += 1


if __name__ == '__main__':
    cases = [
        (
            [0.13, 0.56, 0.23, 0.89, 0.53, 0.91, 0.99, 0, 0.38, 0.47],
            [0, 0.13, 0.23, 0.38, 0.47, 0.53, 0.56, 0.89, 0.91, 0.99]
        )
    ]

    for arr, exp in cases:
        sort(arr)
        assert exp == arr, f"{exp} exp != {arr}"
    print("all cases passed")
