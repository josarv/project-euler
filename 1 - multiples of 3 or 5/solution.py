#!/usr/bin/env python3

def main():
    print(sum([i for i in range(1, 1000) if not i % 3 or not i % 5]))


if __name__ == '__main__':
    main()
