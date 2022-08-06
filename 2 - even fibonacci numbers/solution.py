#!/usr/bin/env python3

def even_fibonacci_terms_up_to(n):
    a, b = 2, 8
    while a <= n:
        yield a
        a, b = b, 4 * b + a


def main():
    print(sum(even_fibonacci_terms_up_to(4_000_000)))


if __name__ == '__main__':
    main()
