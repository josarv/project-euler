#!/usr/bin/env python3

def main():
    n = 600_851_475_143
    i = 2
    while i ** 2 < n:
        while not n % i:
            n //= i
        i += 1
    print(n)


if __name__ == '__main__':
    main()
