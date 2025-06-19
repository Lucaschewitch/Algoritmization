def ff(n, t):
    # первое вхождение
    l, h = 0, len(n) - 1
    f = -1

    while l <= h:
        m = (l + h) // 2  # делим пополам

        if n[m] == t:
            f = m
            h = m - 1
        # меньше - правая
        elif n[m] < t:
            l = m + 1
        # больше - левая
        else:
            h = m - 1

    return f


def fl(n, t):
    # последнее вхождение (то же самое, только знаки поменяем
    l, h = 0, len(n) - 1
    la = -1

    while l <= h:
        m = (l + h) // 2

        if n[m] == t:
            la = m
            l = m + 1
        elif n[m] < t:
            l = m + 1
        else:
            h = m - 1

    return la


def ffl(n, t):
    f = ff(n, t)
    if f == -1:
        return -1
    l = fl(n, t)

    return f, l


if __name__ == "__main__":
    m = input("Введите элементы массива: ")
    n = list(map(int, m.split()))

    t = int(input("Введите искомое число: "))

    # проверка
    if n != sorted(n):
        print("Ошибка: Массив должен быть отсортирован по возрастанию!")
        exit()

    f, l = ffl(n, t)

    # Вывод результата
    if f == -1:
        print(f"Элемент {t} не найден в массиве.")
    else:
        print(f"Первое вхождение элемента {t} на позиции: {f + 1}")
        print(f"Последнее вхождение элемента {t} на позиции: {l + 1}")