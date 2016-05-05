#!/usr/bin/python3
"""Consider concurrent.futures for True Parallelism

Complete!
"""
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


numbers = [(1963309, 2265973), (2030677, 3814172),
           (1551645, 2229620), (2039045, 2020802),
           (1551645, 2229620), (2039045, 2020802),
           (1551645, 2229620), (2039045, 2020802)]


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def main_1():
    start = time.time()
    list(map(gcd, numbers))
    end = time.time()
    return 'Took %.3f seconds' % (end - start)


def main_2():
    start = time.time()
    pool = ThreadPoolExecutor(max_workers=8)
    list(pool.map(gcd, numbers))
    end = time.time()
    return 'Took %.3f seconds' % (end - start)


def main_3():
    start = time.time()
    pool = ProcessPoolExecutor(max_workers=8)
    results = list(pool.map(gcd, numbers))
    end = time.time()
    return 'Took %.3f seconds' % (end - start)


if __name__ == '__main__':
    print(main_1())
    print(main_2())
    print(main_3())