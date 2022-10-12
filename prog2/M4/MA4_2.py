#!/usr/bin/env python3.9
'''
Student: Max Mattsson
mail:
Reviewed by: Xiaoxia
date: 2022-10-12

'''

from person import Person
from numba import njit
from time import perf_counter as timer
import matplotlib.pyplot as plt


@njit
def fib_numba(val):
    if val == 0:
        return 0
    elif val == 1:
        return 1
    else:
        return fib_numba(val - 1) + fib_numba(val - 2)


def fib(val):
    if val == 0:
        return 0
    elif val == 1:
        return 1
    else:
        return fib(val - 1) + fib(val - 2)


def main():
    f = Person(20)
    print(f.get())
    #f.set(47)
    print(f.get())
    f.fib()
    ages = [30, 35, 40]
    py_res = []
    numba_res = []
    c_res = []
    for age in ages:
        f.set(age)
        s = timer()
        py_fib = fib(age)
        py_res.append(py_fib)
        print("python fib of", py_fib, "is", )
        e = timer()
        print(f"time for fib({age}) is {e - s}s with python")

        s = timer()
        num_fib = fib_numba(age)
        numba_res.append(num_fib)
        print("numba fib of", age, "is", num_fib)
        e = timer()
        print(f"time for fib({age}) is {e - s}s with numba")

        s = timer()
        c_fib = f.fib()
        c_res.append(c_fib)
        print("c++ fib of", age, "is", c_fib)
        e = timer()
        print(f"time for fib({age}) is {e - s}s with c++")
    plt.plot(ages, py_res)
    plt.plot(ages, numba_res)
    plt.plot(ages, c_res)
    plt.savefig('fib_results')


if __name__ == '__main__':
    main()
