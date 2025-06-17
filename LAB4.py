import threading  # Для потоков (великолепная штука)
import heapq


def bsort(m, num_threads=1):
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
    n = len(mn)

    # чтоб не тратить время на крайние случаи
    if n <= 1:
        return mn

    # Однопоточная сорт
    if num_threads == 1:  # не люблю длинные названия переменных, но так в условии
        bystraya(mn, 0, n - 1)
        return mn

    # считаем чанки
    nc = min(num_threads, n)
    # Размеры чанков
    cs = n // nc
    c = []
    si = 0
    threads = []  # список потоков

    # Сорт отд чанк
    def sort_chunk(l, h):
        # условие на маленький чанк
        if h - l < 100:
            mn[l:h + 1] = sorted(mn[l:h + 1])
        # условие на большой
        else:
            bystraya(mn, l, h)

    # потоки по чанкам
    for i in range(nc):
        ei = si + cs - 1

        if i == nc - 1:
            ei = n - 1

        # поток для чанка тек
        thread = threading.Thread(target=sort_chunk, args=(si, ei))
        threads.append(thread)
        thread.start()

        c.append((si, ei))
        si = ei + 1

    for thread in threads:
        thread.join()

    # теперь соединяем сорт чанки
    p = [start for start, end in c]
    e = [end for start, end in c]
    h = []
    t = [0] * n

    # куча с первыми эл
    for i in range(len(c)):
        if p[i] <= e[i]:
            heapq.heappush(h, (mn[p[i]], i))
            p[i] += 1

    # мин куча
    index = 0
    while h:
        val, ci = heapq.heappop(h)
        t[index] = val
        index += 1

        # если есть еще то в кучу
        if p[ci] <= e[ci]:
            heapq.heappush(h, (mn[p[ci]], ci))
            p[ci] += 1

    # собсн рез
    mn = t
    return mn


if __name__ == "__main__":
    m = [12, 9, 8, 6, 3, 1]
    num_threads = 2
    mn = bsort(m, num_threads)

    print("Исходный массив:", m)
    print("Отсортированный массив:", mn)
