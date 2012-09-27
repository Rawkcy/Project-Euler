#include <stdio.h>

/*
 * What is the value of the first triangle number to have over five hundred divisors?
 */
int main(int argc, char* argv[]) {
    int factor;
    int factors_count;
    int increment_by = 1;
    int triangle_number = 1;
    while (factors_count <= 500) {
        printf("Factors count is: %d\n", factors_count);
        printf("Increment by is: %d\n", increment_by);
        printf("Triangle number is: %d\n", triangle_number);
        factors_count = 2;  /* 1 and itself */
        increment_by++;
        triangle_number += increment_by;

        /* Find number of factors for new triangle_number */
        for (factor = 2; factor < triangle_number - 1; factor++) {
            if (triangle_number % factor == 0)   factors_count++;
        }
    }
    printf("The triangle with over 500 factors is %d\n", triangle_number);
}

