#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    long sum = 0, a = 1, b = 1, next = 0;
    while (next <= 4000000)
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
