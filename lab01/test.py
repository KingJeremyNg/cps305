import unittest

from mySolution import generate
from mySolution import calcScore

class calcScoreTest(unittest.TestCase) :
    
    def empty(self) :
        result = calcScore([""], [""], 0)
        self.assertEqual(result, 100)

    def equal(self) :
        data = ["a", "b", "c", "d"]
        result = calcScore(data, ["a", "b", "c", "d"], 4)
        self.assertEqual(result, 100)

    def smaller(self) :
        data = ["a", "b", "d", "c"]
        result = calcScore(data, ["a", "b", "c", "d"], 4)
        self.assertEqual(result, 50)

class generateTest(unittest.TestCase) :

    def empty(self) :
        result = generate([""], ["a", "b", "c", "d"], 0, 0, 27, [""])
        self.assertEqual(result , [])
    
    def equal(self) :
        data = ["a", "b", "c", "d"]
        result = generate(data, data, 3, 4, 4, data)
        self.assertEqual(result , ["a", "b", "c", "d"])
    
    def smaller(self) :
        data = ["a", "b", "c", "d"]
        result = generate(data, ["a", "b", "c", "d"], 3, 4, 4, ["a", "c", "d", "b"])
        self.assertEqual(result , ["a", "b", "d", "b"])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)