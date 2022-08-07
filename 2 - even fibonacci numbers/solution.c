#include <stdio.h>
#include <stdlib.h>

#define N 4000000

int main(void)
{
    unsigned long sum = 0, a = 1, b = 1, next = 0;
    while (next <= N)
    {
        next = a + b;
        if (!(next % 2))
            sum += next;
        a = b;
        b = next;
    }
    printf("%ld\n", sum);
    return EXIT_SUCCESS;
}
