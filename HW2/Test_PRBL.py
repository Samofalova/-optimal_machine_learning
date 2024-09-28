import unittest
from sympy import (
    pi, sqrt, tan, sin, cos, log, ln, exp, acos, atan, acot, asin, cot
    )
from PRBL import parabola_method

class TestParabolaMethod(unittest.TestCase):
    def test_0(self):
        res = parabola_method(func='x**2+5', limits=(-100, 100))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0, places=0)
        self.assertAlmostEqual(value_f, 5, places=0)

    def test_1(self):
        res = parabola_method(func='x**3-3*sin(x)', limits=(0, 1), accuracy=10**(-20))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.8, places=1)
        self.assertAlmostEqual(value_f, -1.64, places=2)

    def test_2(self):
        res = parabola_method(func='x**4+x**2+x+1', limits=(-1, 0))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, -0.4, places=1)
        self.assertAlmostEqual(value_f, 0.79, places=2)

    def test_3(self):
        res = parabola_method(func='exp(x)+1/x', limits=(0.5, 1.5))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.7, places=1)
        self.assertAlmostEqual(value_f, 3.44, places=2)

    def test_4(self):
        res = parabola_method(func='x**2-2*x+exp(-x)', limits=(-1, 1.5))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 1.2, places=1)
        self.assertAlmostEqual(value_f, -0.66, places=2)

    def test_5(self):
        res = parabola_method(func='x*sin(x)+2*cos(x)', limits=(-6, -4))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, -4.5, places=1)
        self.assertAlmostEqual(value_f, -4.82, places=2)

    def test_6(self):
        res = parabola_method(func='x+1/x**2', limits=(1, 2))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 1.3, places=1)
        self.assertAlmostEqual(value_f, 1.89, places=2)

    def test_7(self):
        res = parabola_method(func='10*x*ln(x)-x**2/2', limits=(0.1, 1))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.5, places=1)
        self.assertAlmostEqual(value_f, -3.7, places=1)

    def test_8(self):
        res = parabola_method(func='exp(x)-1/3*x**3+2*x', limits=(-2.5, -1))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, -1.5, places=1)
        self.assertAlmostEqual(value_f, -1.65, places=2)

    def test_9(self):
        res = parabola_method(func='x**2-2*x-2*cos(x)', limits=(-0.5, 1))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.5, places=1)
        self.assertAlmostEqual(value_f, -2.51, places=2)

    def test_10(self):
        res = parabola_method(func='exp(x)-1-x-x**2/2-x**3/6', limits=(-5, 5))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.0, places=1)
        self.assertAlmostEqual(value_f, 0.00, places=2)

    def test_11(self):
        res = parabola_method(func='x**(exp(0.1*x)*sin(x))', limits=(2.5, 14))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 5, places=0)
        self.assertAlmostEqual(value_f, 0.1, places=1)

    def test_12(self):
        res = parabola_method(func='-5*x**5+4*x**4-12*x**3+11*x**2-2*x+1', limits=(-0.5, 0.5))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.1, places=1)
        self.assertAlmostEqual(value_f, 0.9, places=1)

    def test_13(self):
        res = parabola_method(func='-(ln(x-2))**2 + (ln(10-x))**2-x**(1/5)', limits=(6, 9.9))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 9.2, places=1)
        self.assertAlmostEqual(value_f, -5.41, places=2)

    def test_14(self):
        res = parabola_method(func='-3*x*sin(0.75*x)+exp(-2*x)', limits=(0, 2*pi))
        point = res[1]
        value_f = res[0]
        self.assertGreaterEqual(point, 2)
        self.assertLessEqual(point, 3.5)
        self.assertAlmostEqual(value_f, -7, places=0)

    def test_15(self):
        res = parabola_method(func='exp(3*x)+5*exp(-2*x)', limits=(0, 1))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 0.2, places=1)
        self.assertAlmostEqual(value_f, 5.15, places=2)

    def test_16(self):
        res = parabola_method(func='0.2*x*ln(x)+(x-2.3)**2', limits=(0.5, 2.5))
        point = res[1]
        value_f = res[0]
        self.assertAlmostEqual(point, 2.1, places=1)
        self.assertAlmostEqual(value_f, 0.35, places=2)

    def test_17(self):
        res = parabola_method(func='-1/((x-1)**2)*(log(x)-2*(x-1)/(x+1))', limits=(1.5, 4.5), accuracy=10**(-20))
        point = res[1]
        value_f = res[0]
        self.assertGreaterEqual(point, 2.5)
        self.assertLessEqual(point, 4)
        self.assertAlmostEqual(value_f, -0.03, places=2)

if __name__ == '__main__':
    unittest.main()
