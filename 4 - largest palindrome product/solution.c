#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define N 1000

bool is_palindrome(unsigned long num);

int main(void)
{
    unsigned long max = 9009, product;
    for (unsigned long i = 100; i < N; i++)
    {
        for (unsigned long j = 100; j < N; j++)
        {
            product = i * j;
            if (product > max && is_palindrome(product))
                max = product;
        }
    }
    printf("%lu\n", max);
    return EXIT_SUCCESS;
}

bool is_palindrome(unsigned long num)
{
    unsigned long n = num, reversed = 0;
    while (n)
    {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    return num == reversed;
}
