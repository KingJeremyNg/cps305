import unittest

from mySolution import infixToPostfixEval

class tester(unittest.TestCase) :

    def testEmpty(self) :
        result = infixToPostfixEval('')
        self.assertEqual(result, 'Empty expression')

    def testNormal(self) :
        result = infixToPostfixEval('5 + ( 3 - 5 ) * 2')
        self.assertEqual(result, '5 3 5 - 2 * +\nEvaluates to: 1')

    def testExtreme(self) :
        result = infixToPostfixEval('( 1 ! + 2 ! + 3 ! ) * 9 + ( 4 ! + 5 ! ) * 9 !')
        self.assertEqual(result, '1 ! 2 ! + 3 ! + 9 * 4 ! 5 ! + 9 ! * +\nEvaluates to: 52254801')

    def testMix(self) :
        result = infixToPostfixEval('3 ! * ( 3 + ( 7 ! / 9 + ( 5 * 2 ) ) )')
        self.assertEqual(result, '3 ! 3 7 ! 9 / 5 2 * + + *\nEvaluates to: 3438.0')

    def testNegative(self) :
        result = infixToPostfixEval('( 6 * 7 + 4 ) * 2 * ( 8 - 3 * 9 )')
        self.assertEqual(result, '6 7 * 4 + 2 * 8 3 9 * - *\nEvaluates to: -1748')

if __name__ == '__main__' :
    unittest.main(argv = ['firt-arg-is-ignored'], exit = False)