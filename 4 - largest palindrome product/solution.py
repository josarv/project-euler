#!/usr/bin/env python3


def main():
    maximum = 1
    for i in range(1, 999):
        for j in range(1, 999):
            product = i * j
            if product > maximum:
                s = str(product)
                if s == s[::-1]:
                    maximum = product
    print(maximum)


if __name__ == '__main__':
    main()
