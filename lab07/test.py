import unittest
from eval import evalTree


class tester(unittest.TestCase):
    def testOne(self):
        result = evalTree(["1", [], []], [])
        self.assertEqual(result, 1)

    def testAddition(self):
        result = evalTree(["+", ["a", [], []], ["b", [], []]], [["a", 10], ["b", 20]])
        self.assertEqual(result, 30)

    def testSubtraction(self):
        result = evalTree(["-", ["b", [], []], ["a", [], []]], [["a", 10], ["b", 20]])
        self.assertEqual(result, 10)

    def testMultiplication(self):
        result = evalTree(["*", ["a", [], []], ["b", [], []]], [["a", 10], ["b", 20]])
        self.assertEqual(result, 200)

    def testDivision(self):
        result = evalTree(["/", ["a", [], []], ["b", [], []]], [["a", 10], ["b", 20]])
        self.assertEqual(result, 0.5)

    def testChild(self):
        result = evalTree(["+", ["a", [], []], ["*", ["b", [], []], ["c", [], []]]], [["a", 10], ["b", 20], ["c", 30]])
        self.assertEqual(result, 610)

    def testChildMulti(self):
        result = evalTree(["+", ["a", [], []], ["*", ["+", ["a", [], []], ["a", [], []]], ["c", [], []]]], [["a", 10], ["b", 20], ["c", 30]])
        self.assertEqual(result, 610)

    def testEmpty(self):
        result = evalTree([[], [], []], [])
        self.assertEqual(result, None)
    
    def testZeroDivision(self):
        result = evalTree(["/", ["a", [], []], ["0", [], []]], [["a", 10]])
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
