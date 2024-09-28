import pandas as pd
import numpy as np
from sympy import *
from copy import deepcopy


# пока оставил
def get_data():
    '''
    Function for get data from user.
    '''

    func = input('Введите функцию в аналитическом виде (Например: x + 1): ')
    limits = eval(input('Введите границы области оптимизации в виде списка (Например: [1, 3]): '))

    return funct, limits


# основная функция решения
def parabola_method(func: str,
                    limits: list,
                    accuracy: float = 10 ** (-5),
                    max_iterations: int = 500,
                    intermediate_results: bool = False,
                    intermediate_writing: bool = False):
    """
    Search for the extremum of a function of one variable using the parabola method.

    args:
        mandatory:
            - func - function in analytical form;
            - limits - optimization area boundaries;
        optional:
            - accuracy - optimization precision by argument (default: 10^-5);
            - max_iterations - maximum number of iterations (default: 500;
            - intermediate_results - flag "output intermediate results" (default: False);
            - intermediate_writing - flag "writing intermediate results to dataset" (default: False);

    outputs:
        - The found value of the extremum point coordinate;
        - Function value at the extremum point;
        - Algorithm report;
    """

    x = symbols('x')
    F = eval(func)

    left_hand, right_hand = limits

    left_hand = float(left_hand)
    right_hand = float(right_hand)

    if left_hand > right_hand:
        left_hand, right_hand = right_hand, left_hand

    iteration_num = 0
    d = 100
    while (d > accuracy) or (iteration_num < max_iterations):
        # need to satisfy inequality x1<x2<x3, f(x1) >= f(x2) <= f(x3)

        # first step
        if iteration_num == 0:
            x1 = left_hand
            x3 = right_hand
            x2 = (x1 + x3) / 2

        f1 = F.subs(x, x1)
        f2 = F.subs(x, x2)
        f3 = F.subs(x, x3)

        # return f1

        # second step

        # first  formula - a0 = f1, a1 = (f2-f1)/(x2-x1), a2 = 1/(x3-x2) * ((f3-f1)/(x3-x1) - (f2-f1)/(x2-x1))
        # second formula - x_ = 1/2*(x1 + x2 - a1/a2)
        a0 = float(deepcopy(f1))
        a1 = float((f2 - f1) / (x2 - x1))
        a2 = float(1 / (x3 - x2) * ((f3 - f1) / (x3 - x1) - (f2 - f1) / (x2 - x1)))

        if iteration_num > 0:
            x_old = deepcopy(x_)

        x_ = 1 / 2 * (x1 + x2 - a1 / a2)

        # check num of step - go to step 4 if its first step
        if iteration_num > 0:
            d = abs(x_old - x_)

            if d <= accuracy:
                x_res = deepcopy(x_)

        # step 4
        f_x_ = F.subs(x, x_)

        # step 5
        # suppose x1 = x_ = ..., f1 = f_x_ = ...
        if x1 < x_ < x2 < x3 and f_x_ >= f2:  # x* in [x_, x3]
            x1 = deepcopy(x_)
            f1 = deepcopy(f_x_)
        elif x1 < x2 < x_ < x3 and f2 >= f_x_:  # x* in [x2, x3]
            x1 = deepcopy(x2)
            f1 = deepcopy(f2)
            x2 = deepcopy(x_)
            f2 = deepcopy(f_x_)

        iteration_num += 1

    f_res = F.subs(x, x_res)

    return f_res, x_res, iteration_num
