def factorial(n: int) -> int:
    if n<0:
        return "Undefined for negative integers"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

input = int(input())
print(f"The factorial of {input} is: {factorial(input)}")
