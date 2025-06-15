import numpy as np
import unittest


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


a, b = 6, 8
n = 1000
a = simpson_rule(oblast, a, b, n)


class TestSimpsonRule(unittest.TestCase):
    def test_linear_function(self):
        f = lambda x: x
        result = simpson_rule(f, 0, 1, 100)
        self.assertAlmostEqual(result, 0.5, delta=1e-6)

    def test_quadratic_function(self):
        f = lambda x: x ** 2
        result = simpson_rule(f, 0, 1, 100)
        self.assertAlmostEqual(result, 1 / 3, delta=1e-6)

    def test_sin_function(self):
        f = lambda x: np.sin(x)
        result = simpson_rule(f, 0, np.pi, 100)
        self.assertAlmostEqual(result, 2.0, delta=1e-6)


if __name__ == "__main__":
    unittest.main()

print(f"Метод Симпсона: {a:.4f}")
