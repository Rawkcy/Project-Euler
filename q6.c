#include <stdio.h>
#include <math.h>

/* 
 * Find the difference between the sum of the squares of
 * the first one hundred natural numbes and the square of the sum
 */
 
int main(int argc, char* argv[]) {
    int sum, sum_of_squares = 0;
    int i;
    for (i = 0; i <= 100; i++) {
        sum += i;
        sum_of_squares += i*i;
    }
    printf("The difference is %d\n", abs(sum*sum - sum_of_squares));
}

