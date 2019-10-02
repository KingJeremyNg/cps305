import unittest

from mySolution import power, powerH, bCoefficient

class tester(unittest.TestCase) :

    def testPowerNormal(self) :
        resultA = power(2, 2)
        resultB = powerH(2, 2)
        self.assertEqual(resultA, 4)
        self.assertEqual(resultB, 4)
    
    def testPowerExtreme(self) :
        resultA = power(2, 100)
        resultB = powerH(2, 100)
        self.assertEqual(resultA, 1267650600228229401496703205376)
        self.assertEqual(resultB, 1267650600228229401496703205376)
    
    def testPowerNegative(self) :
        resultA = power(2, -1)
        resultB = powerH(2, -1)
        self.assertEqual(resultA, "Invalid input")
        self.assertEqual(resultB, "Invalid input")
    
    def testPowerZero(self) :
        resultA = power(2, 0)
        resultB = powerH(2, 0)
        self.assertEqual(resultA, 1)
        self.assertEqual(resultB, 1)
    
    def testPowerOne(self) :
        resultA = power(2, 1)
        resultB = powerH(2, 1)
        self.assertEqual(resultA, 2)
        self.assertEqual(resultB, 2)
    
    def testCoefficientNormal(self) :
        result = bCoefficient(2, 1)
        self.assertEqual(result, 2)
    
    def testCoefficientExtreme(self) :
        result = bCoefficient(10, 5)
        self.assertEqual(result, 252)

    def testCoefficientNegative(self) :
        result = bCoefficient(5, -3)
        self.assertEqual(result, "Invalid input")
    
    def testCoefficientZero(self) :
        result = bCoefficient(0, 0)
        self.assertEqual(result, 1)
    
    def testCoefficientEqual(self) :
        result = bCoefficient(5, 5)
        self.assertEqual(result, 1)    

if __name__ == '__main__' :
    unittest.main(argv = ['first-arg-is-ignored'], exit = False)