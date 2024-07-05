def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)

def gcdWithDiv(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return b if a % b == 0 else gcdWithDiv(a-b, b)
    else:
        return a if b % a == 0 else gcdWithDiv(a, b-a)

def gcdWithMod(a, b):
    return a if b == 0 else gcdWithMod(b, a % b)


if __name__ == '__main__':
    a, b = map(int, input().rstrip().split())
    result = gcd(a, b)
    resultWithDiv = gcdWithDiv(a, b)
    resultWithMod = gcdWithMod(a, b)
    print('a:', a, 'b:', b)
    print('result:', result)
    print('resultWithDiv:', resultWithDiv)
    print('resultWithMod:', resultWithMod)
