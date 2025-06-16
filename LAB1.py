import sys
import time
import unittest


def setremove(s, e):
    sm = sys.getsizeof(s)
    st = time.perf_counter()

    s.remove(e)

    et = time.perf_counter()
    em = sys.getsizeof(s)

    tt = et - st
    m = sm - em

    return tt, m


class TestSetRemove(unittest.TestCase):
    def test_element_removal(self):
        s = {1, 2, 3, 4, 5}
        ssb = len(s)
        setremove(s, 3)
        self.assertNotIn(3, s)
        self.assertEqual(len(s), ssb - 1)

    def test_memory_consumption(self):
        s = set(range(1000))
        _, mem_raz = setremove(s, 500)
        self.assertIsInstance(mem_raz, int)

    def test_time_measurement(self):
        s = set(range(100000))
        tt, _ = setremove(s, 99999)
        self.assertGreaterEqual(tt, 0)


if __name__ == "__main__":

    s = set(range(1000000))
    e = 1

    print(f"Начальный размер множества: {len(s)}")
    print(f"Начальный объем памяти: {sys.getsizeof(s)} байт")

    tt, m = setremove(s, e)

    print(f"\nВремя удаления элемента: {tt:.10f} секунд")
    print(f"Изменение потребления памяти: {m} байт")
    print(f"Конечный размер множества: {len(s)}")
    print(f"Конечный объем памяти: {sys.getsizeof(s)} байт")

    unittest.main(argv=[''], exit=False)