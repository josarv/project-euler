#include <stdbool.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define N 600851475143

bool is_prime(unsigned long n);

int main(void)
{
    unsigned long max = 0;
    for (unsigned long i = 2; i < (unsigned long) sqrt((double)N); i++)
    {
        if (is_prime(i) && !(N % i))
            max = i;
    }
    printf("%lu\n", max);
    return EXIT_SUCCESS;
}

bool is_prime(unsigned long n)
{
    for (unsigned long i = 2; i <= (unsigned long)sqrt((double)n) ; i++)
    {
        if (!(n % i))
            return false;
    }
    return true;
}
