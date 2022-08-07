#include <stdio.h>
#include <stdlib.h>

#define N 1000

int main(void)
{
    unsigned long sum = 0;
    for (unsigned long i = 0; i < N; i++)
    {
        if (!(i % 3) || !(i % 5))
            sum += i;
    }
    printf("%ld", sum);
    return EXIT_SUCCESS;
}
