from sympy import *
from copy import deepcopy
from PRBL import parabola_method


def BrantMethod(func: str,
                limits: list,
                accuracy: float = 10 ** (-5),
                max_iterations: int = 500,
                intermediate_results: bool = False,
                intermediate_writing: bool = False):
    X = symbols('x')
    F = eval(func)

    a, b = eval(limits)
    r = (3 - 5 ** (1 / 2)) / 2

    x = a + r * (b - a)
    w = a + r * (b - a)
    v = a + r * (b - a)

    f_x = F.subs(X, x)
    f_w = F.subs(X, w)
    f_v = F.subs(X, v)

    d_cur = b - a
    d_prv = b - a

    step_num = 0
    while step_num <= max_iterations:
        if max(abs(x - a), abs(b - x)) < accuracy:
            return x, F.subs(X, x)
        g = d_prv / 2
        d_prv = deepcopy(d_cur)
        #         res = solve([f_x - a0*x**2 - a1*x - a2, f_w - a0*w**2 - a1*w -a2, f_v - a0*v**2 - a1*v - a2],
        #                          [a0, a1, a2], dict=True)[0]
        #         u = -res[a1]/(2*res[a0])
        u = parabola_method(func, limits)
        if u is None or not (a <= u <= b) or abs(u - x) > g:
            if x < (a + b) / 2:
                u = x + r * (b - x)
                d_prv = b - x
            else:
                u = x - r * (x - a)
                d_prv = x - a
        d_cur = abs(u - x)
        if F.subs(X, u) > f_x:
            if u < x:
                a = deepcopy(u)
            else:
                b = deepcopy(u)
            if F.subs(X, u) <= f_w or w == x:
                v = deepcopy(w)
                w = deepcopy(u)
            else:
                if F.subs(X, u) <= f_v or v == x or v == w:
                    v = deepcopy(u)
        else:
            if u < x:
                b = deepcopy(x)
            else:
                a = deepcopy(x)
            v = deepcopy(w)
            w = deepcopy(x)
            x = deepcopy(u)

    return x