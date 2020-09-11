from math import floor


def mcd(x, y):
    if x < y:
        return mcd(y, x)

    while y != 0:
        x, y = y, x % y

    return x


print(mcd(25, 2))
print(mcd(99, 88))
print(mcd(1506, 3046))

