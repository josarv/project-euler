#!/usr/bin/env python3

import math


def fibonacci(n):
    return round(pow((1 + math.sqrt(5)) / 2, n) / math.sqrt(5))


def main():
    total = 0
    n = 0
    while True:
        next_term = fibonacci(n)
        if next_term > 4000000:
            break
        if next_term % 2 == 0:
            total += next_term
        n += 3
    print(total)


if __name__ == '__main__':
    main()
