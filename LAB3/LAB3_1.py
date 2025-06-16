def sliyaniye(m):
    if len(m) > 1:
        ser = len(m) // 2
        l = m[:ser]
        r = m[ser:]

        sliyaniye(l)
        sliyaniye(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                m[k] = l[i]
                i += 1
            else:
                m[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            m[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            m[k] = r[j]
            j += 1
            k += 1

if __name__ == "__main__":
    m = [38, 27, 43, 3, 9, 89, 10]
    print("Исходный массив:", m)

    sliyaniye(m)
    print("Отсортированный массив:", m)
