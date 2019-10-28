import unittest
from sorting import mo3_quickSort


class tester(unittest.TestCase):
    def testNormal(self):
        list = [5, 4, 3, 2, 1]
        mo3_quickSort(list)
        self.assertEqual(list, [1, 2, 3, 4, 5])

    def testOne(self):
        list = [1]
        mo3_quickSort(list)
        self.assertEqual(list, [1])

    def testEmpty(self):
        list = []
        mo3_quickSort(list)
        self.assertEqual(list, [])

    def testSame(self):
        list = [2, 2, 2]
        mo3_quickSort(list)
        self.assertEqual(list, [2, 2, 2])

    def testSameMulti(self):
        list = [5, 5, 5, 1, 1, 1, 10, 10, 10]
        mo3_quickSort(list)
        self.assertEqual(list, [1, 1, 1, 5, 5, 5, 10, 10, 10])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
