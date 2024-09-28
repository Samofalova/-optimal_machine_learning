import unittest
from sympy import (
    pi, sqrt, tan, sin, cos, log, ln, exp, acos, atan, acot, asin, cot
    )
from BRNT import BrantMethod

class TestBrantMethod(unittest.TestCase):
    def test_0(self):
        res = BrantMethod(func='x**2+5', limits='[-100, 100]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0, places=0)
        self.assertAlmostEqual(value_f, 5, places=0)

    def test_1(self):
        res = BrantMethod(func='x**3-3*sin(x)', limits='[0, 1]', accuracy=10**(-20))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.82413, places=5)
        self.assertAlmostEqual(value_f, -1.64213, places=5)

    def test_2(self):
        res = BrantMethod(func='x**4+x**2+x+1', limits='[-1, 0]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, -0.38546, places=5)
        self.assertAlmostEqual(value_f, 0.78520, places=5)

    def test_3(self):
        res = BrantMethod(func='exp(x)+1/x', limits='[0.5, 1.5]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.70347, places=5)
        self.assertAlmostEqual(value_f, 3.4423, places=4)

    def test_4(self):
        res = BrantMethod(func='x**2-2*x+exp(-x)', limits='[-1, 1.5]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 1.1572, places=4)
        self.assertAlmostEqual(value_f, -0.66092, places=5)

    def test_5(self):
        res = BrantMethod(func='x*sin(x)+2*cos(x)', limits='[-6, -4]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, -4.49341, places=5)
        self.assertAlmostEqual(value_f, -4.82057, places=5)

    def test_6(self):
        res = BrantMethod(func='x+1/x**2', limits='[1, 2]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 1.2599, places=4)
        self.assertAlmostEqual(value_f, 1.8899, places=4)

    def test_7(self):
        res = BrantMethod(func='10*x*ln(x)-x**2/2', limits='[0.1, 1]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.38221, places=5)
        self.assertAlmostEqual(value_f, -3.7491, places=4)

    def test_8(self):
        res = BrantMethod(func='exp(x)-1/3*x**3+2*x', limits='[-2.5, -1]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, -1.49165, places=5)
        self.assertAlmostEqual(value_f, -1.65198, places=5)

    def test_9(self):
        res = BrantMethod(func='x**2-2*x-2*cos(x)', limits='[-0.5, 1]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.51097, places=5)
        self.assertAlmostEqual(value_f, -2.50539, places=5)

    def test_10(self):
        res = BrantMethod(func='exp(x)-1-x-x**2/2-x**3/6', limits='[-5, 5]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.000, places=3)
        self.assertAlmostEqual(value_f, 0.000000, places=5)

    def test_11(self):
        res = BrantMethod(func='x**(exp(0.1*x)*sin(x))', limits='[2.5, 14]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 8.01261, places=5)
        self.assertAlmostEqual(value_f, 97.4179, places=4)

    def test_12(self):
        res = BrantMethod(func='-5*x**5+4*x**4-12*x**3+11*x**2-2*x+1', limits='[-0.5, 0.5]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.10986, places=5)
        self.assertAlmostEqual(value_f, 0.897633, places=6)

    def test_13(self):
        res = BrantMethod(func='-(ln(x-2))**2 + (ln(10-x))**2-x**(1/5)', limits='[6, 9.9]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 9.20624, places=5)
        self.assertAlmostEqual(value_f, -5.40596, places=5)

    def test_14(self):
        res = BrantMethod(func='-3*x*sin(0.75*x)+exp(-2*x)', limits='[0, 2*pi]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 2.70648, places=5)
        self.assertAlmostEqual(value_f, -7.27436, places=5)

    def test_15(self):
        res = BrantMethod(func='exp(3*x)+5*exp(-2*x)', limits='[0, 1]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.24079, places=5)
        self.assertAlmostEqual(value_f, 5.1483, places=4)

    def test_16(self):
        res = BrantMethod(func='0.2*x*ln(x)+(x-2.3)**2', limits='[0.5, 2.5]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 2.1246, places=4)
        self.assertAlmostEqual(value_f, 0.35098, places=5)

    def test_17(self):
        res = BrantMethod(func='-1/((x-1)**2)*(log(x)-2*(x-1)/(x+1))', limits='[1.5, 4.5]')
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 2.1887, places=4)
        self.assertAlmostEqual(value_f, -0.02671, places=5)

if __name__ == '__main__':
    unittest.main()