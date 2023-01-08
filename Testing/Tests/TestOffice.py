import unittest
from Office import employer

class TestSalaryCase(unittest.TestCase):
    
    def setUp(self):
        name = "tim"
        uname = "wilburg"
        salary = 5000
        self.emp = employer(name, uname, salary)

    def test_getRaise_default(self):
        self.emp.getRaise()
        self.assertequal(salary, 10000)

    def test_getRaise_custom(self):
        self.emp.getRaise(10000)
        self.assertequal(salary, 20000)

unittest.main()

