#!/usr/bin/env python3

from itertools import product


def main():
    print(max(filter(lambda x: str(x) == str(x)[::-1], map(lambda x: x[0] * x[1], product(range(100, 1000), repeat=2)))))


if __name__ == '__main__':
    main()
