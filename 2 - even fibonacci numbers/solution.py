import math


def fibonacci(n):
    return round(pow((1 + math.sqrt(5)) / 2, n) / math.sqrt(5))


def main():
    sum = 0
    n = 0
    while True:
        next = fibonacci(n)
        if next > 4000000:
            break
        if next % 2 == 0:
            sum += next
        n += 3
    print(sum)


if __name__ == '__main__':
    main()
