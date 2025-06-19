M = int(input())  # Грузоподъемность
n = int(input())  # Колво куч
p = []

for i in range(n):
    ci, mi = map(int, input().split())
    # делаем кортеж peska
    p.append((ci, mi))

# по убыванию сорт, чтоб самый дорогой песок был в начале
p.sort(key=lambda x: x[0], reverse=True)

total_value = 0
capacity_left = M

for ci, mi in p:
    if capacity_left <= 0:
        break

    # либо всё, либо сколько сможет унести Гоша
    take = min(mi, capacity_left)

    # считаем франки
    total_value += ci * take
    capacity_left -= take

print(total_value)
