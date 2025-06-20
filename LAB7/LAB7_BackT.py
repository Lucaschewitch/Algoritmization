def norm(v, c, m, cs):
    # проверяем, норм ли назначить цвет
    n = len(m)
    for i in range(n):
        # проверка есть ребо, не занят цвет
        if m[v][i] == '1' and cs[i] == c:
            return False
    return True


def bt(v, cs, m, n, k):
    # все раскрашены
    if v == n:
        return True

    for color in range(1, k + 1):
        # норм ли этот цвет
        if norm(v, color, m, cs):
            cs[v] = color
            if bt(v + 1, cs, m, n, k):
                return True

            # если нет решения, делаем откат
            cs[v] = 0

    # нет цвета
    return False


def main():
    n, k = map(int, input().split())
    m = [input().strip() for _ in range(n)]

    # чтоб не было петель
    for i in range(n):
        if m[i][i] == '1':
            print("NO")
            return

    cs = [0] * n

    if bt(0, cs, m, n, k):
        print("YES")
        print(" ".join(map(str, cs)))
    else:
        print("NO")


if __name__ == "__main__":
    main()
