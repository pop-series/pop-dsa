def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def gcdWithDiv(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    while a != b:
        if a > b:
            if a % b == 0:
                return b
            a -= b
        else:
            if b % a == 0:
                return a
            b -= a
    return a

def gcdWithMod(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    a, b = map(int, input().rstrip().split())
    result = gcd(a, b)
    resultWithDiv = gcdWithDiv(a, b)
    resultWithMod = gcdWithMod(a, b)
    print('a:', a, 'b:', b)
    print('result:', result)
    print('resultWithDiv:', resultWithDiv)
    print('resultWithMod:', resultWithMod)

