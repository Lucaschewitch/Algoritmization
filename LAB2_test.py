import unittest
import numpy as np
from LAB2 import simpson_rule  # Импорт из основного модуля


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
