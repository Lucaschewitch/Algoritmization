import numpy as np


def f1(x):
    return np.sin(x)


def f2(x):
    return np.cos(x)


def f3(x):
    return np.sin(0.5 * x) - 0.5


def oblast(x):
    y1, y2, y3 = f1(x), f2(x), f3(x)
    mx = np.maximum(np.maximum(y1, y2), y3)
    mn = np.minimum(np.minimum(y1, y2), y3)
    return mx - mn


def simpson_rule(f, a, b, n):
    if n % 2 == 1:
        n += 1  # Делаем n четным
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = f(x)

    integral = (h / 3) * (fx[0] + 4 * sum(fx[1:-1:2]) + 2 * sum(fx[2:-2:2]) + fx[-1])
    return integral


if __name__ == "__main__":
    a, b = 6, 8
    n = 1000
    result = simpson_rule(oblast, a, b, n)
    print(f"Метод Симпсона: {result:.4f}")