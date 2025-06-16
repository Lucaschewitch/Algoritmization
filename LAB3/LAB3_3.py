def bsort(m):
    def bystraya(n, l, h):
        if l < h:
            oi = part(n, l, h)
            bystraya(n, l, oi - 1)
            bystraya(n, oi + 1, h)

    def part(n, l, h):
        o = n[h]
        i = l - 1

        for j in range(l, h):
            if n[j] <= o:
                i += 1
                n[i], n[j] = n[j], n[i]

        n[i + 1], n[h] = n[h], n[i + 1]
        return i + 1

    mn = list(m)
    bystraya(mn, 0, len(mn) - 1)
    return mn


if __name__ == "__main__":
    m = [3, 6, 8, 10, 1, 2, 12]
    mn = bsort(m)
    print("Исходный массив:", m)
    print("Отсортированный массив:", mn)
