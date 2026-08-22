#include <stdio.h>

int main() {
    int n;
    int factorial = 1;

    printf("Enter a number: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        factorial *= i;
    }

    printf("Factorial: %d\n", factorial);

    return 0;
}
