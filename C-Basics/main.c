#include <stdio.h>
#include "calculator.h"

int main()
{
    int a = 10;
    int b = 5;

    printf("Welcome to C Basics!\n");

    printf("Addition: %d\n", add(a, b));
    printf("Subtraction: %d\n", subtract(a, b));
    printf("Multiplication: %d\n", multiply(a, b));

    if(b!=0){
        printf("Division: %d\n", divide(a, b));  # Missing check for b==0
    }
    else{
        printf("You can divide a number by 0");
    }
    return 0;
}
