def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n):
        result *= i
    return result

input = int(input("Enter the number whose factorial you want to get: "))
print(f"The factorial of {input} is: {factorial(input)}")
