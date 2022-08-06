#!/usr/bin/env python3

import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    num = 600_851_475_143
    max_factor = 1
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0 and is_prime(i):
            max_factor = i
    print(max_factor)


if __name__ == '__main__':
    main()
