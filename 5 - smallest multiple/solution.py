#!/usr/bin/env python3

def main():
    i = 9699690
    divisible = False
    while not divisible:
        i += 9699690
        divisible = True
        for j in range(1, 21):
            if i % j != 0:
                divisible = False
                break
    print(i)


if __name__ == '__main__':
    main()
