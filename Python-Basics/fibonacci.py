def fibonacci(n):
    sequence = []

    a = 1
    b =1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence  # Will produce wrong sequence starting from 0, 1, 1...


def main():
    n = int(input("Enter number of terms: "))

    if n < 0:
        print("Invalid input")
        return

    print("Fibonacci sequence:")
    print(fibonacci(n))


if __name__ == "__main__":
    main()
