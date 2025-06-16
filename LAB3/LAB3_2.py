def porazsort(m):
    if len(m) <= 1:
        return m

    mx = max(m)
    r = 1

    while mx // r > 0:
        m = sortporaz(m, r)
        r *= 10
    return m


def sortporaz(m, r):
    k = [[] for _ in range(10)]

    for n in m:
        i = (n // r) % 10
        k[i].append(n)

    sm = []
    for k1 in k:
        sm.extend(k1)
    return sm


if __name__ == "__main__":
    m = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Исходный массив:", m)
    sm = porazsort(m)
    print("Отсортированный массив:", sm)
