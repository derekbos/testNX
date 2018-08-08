import unittest
from functionfail import fun
class MyTest(unittest.TestCase):
    def test(self):
       if (fun(3)==4):
            print("okay")
       else:
            exit()
if __name__ == '__main__':
    unittest.main()
