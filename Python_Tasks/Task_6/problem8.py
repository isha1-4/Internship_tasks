def old_tuple_hash(values):
    mask = (1 << 64) - 1
    x = 0x345678
    mult = 1000003
    n = len(values)

    for i, value in enumerate(values):
        remaining = n - i - 1
        x = ((x ^ value) * mult) & mask
        mult = (mult + 82520 + 2 * remaining) & mask

    x = (x + 97531) & mask

    if x == mask:
        x = 1546275796

    if x >= (1 << 63):
        x -= (1 << 64)

    return x

if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    print(old_tuple_hash(t))
