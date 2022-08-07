#!/usr/bin/env python3

from itertools import product


def main():
    print(max(i * j for i, j in product(range(100, 1000), repeat=2) if str(i * j) == str(i * j)[::-1]))


if __name__ == '__main__':
    main()
