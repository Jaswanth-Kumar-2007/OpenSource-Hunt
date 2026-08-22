#include <stdio.h>

int main() {
    int n;
    int isPrime = 1;

    printf("Enter a number: ");
    scanf("%d", &n);

    if (n==0 || n==1) {
        isPrime = 0;
    } else

    if (n < 2) {
        isPrime =0;
    }

    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            isPrime = 0;
            break;
        }
    }

    if (isPrime)
        printf("%d is prime\n", n);
    else
        printf("%d is not prime\n", n);

    return 0;
}
