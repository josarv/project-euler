#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    long sum = 0;
    for (long i = 0; i < 1000; i++)
    {
        if (!(i % 3) || !(i % 5))
            sum += i;
    }
    printf("%ld", sum);
    return EXIT_SUCCESS;
}
