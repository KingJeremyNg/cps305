import unittest
from parserTools import parse


class tester(unittest.TestCase):
    
    def testEmpty(self):
        result = parse([])
        self.assertEqual(result, [])

    def testOne(self):
        result = parse(['1'])
        self.assertEqual(result, ['1', [], []])

    def testFactorial(self):
        result = parse(['2', '!'])
        self.assertEqual(result, ['!', ['2', [], []], []])

    def testList(self):
        result = parse([['4', '+', '3'], '*', '7'])
        self.assertEqual(result, ['*', ['+', ['4', [], []], ['3', [], []]], ['7', [], []]])

    def testLongList(self):
        result = parse([['4', '+', '3'], '*', '7', '+', ['4', '+', [['3', '+', '1'], '!']]])
        self.assertEqual(result, ['+', ['*', ['+', ['4', [], []], ['3', [], []]], ['7', [], []]], ['+', ['4', [], []], ['!', ['+', ['3', [], []], ['1', [], []]], []]]])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
