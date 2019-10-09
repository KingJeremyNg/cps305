import unittest
from mySolution import HashTable

class tester(unittest.TestCase) :
    def testNormal(self) :
        H = HashTable()
        H[1] = "cat"
        H[2] = "dog"
        H[3] = "chicken"
        self.assertEqual(H.data[3], "chicken")
    
    def testCollision(self) :
        H = HashTable()
        H[1] = "cat"
        H[2] = "dog"
        H[3] = "duck"
        H[14] = "chicken"
        self.assertEqual(H.data[4], "chicken")
    
    def testResize(self) :
        H = HashTable()
        H[1] = "cat"
        H[2] = "dog"
        H[3] = "duck"
        H[4] = "lion"
        H[5] = "tiger"
        H[6] = "bird"
        H[7] = "cow"
        H[8] = "goat"
        H[20] = "chicken"
        self.assertEqual(H.data[20], "chicken")
    
    def testEmpty(self) :
        H = HashTable()
        H[1] = "cat"
        H[2] = "dog"
        H[3] = "duck"
        H[4] = ""
        self.assertEqual(H.slots[4], None)
        self.assertEqual(H.data[4], None)
    
    def testOverwrite(self) :
        H = HashTable()
        H[1] = "cat"
        H[2] = "dog"
        H[3] = "duck"
        H[3] = "chicken"
        self.assertEqual(H.data[3], "chicken")

if __name__ == '__main__' :
    unittest.main(argv = ['first-arg-is-ignored'], exit = False)