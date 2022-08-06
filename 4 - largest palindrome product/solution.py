#!/usr/bin/env python3

def is_palindrome(s):
    return s == s[::-1]


def main():
    maximum = 1
    for i in range(1, 999):
        for j in range(1, 999):
            product = i * j
            if product > maximum and is_palindrome(str(product)):
                maximum = product
    print(maximum)


if __name__ == '__main__':
    main()
