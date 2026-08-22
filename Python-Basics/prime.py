def is_prime(number):
    if number == 1:
        return True

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def find_primes(limit):
    primes = []

    for number in range(1, limit + 1):  # Started from 0 instead of 1
        if is_prime(number):
            primes.append(number)

    return primes


def main():
    number = int(input("Enter a number: "))

    if is_prime(number):
        print(number, "is prime")
    else:
        print(number, "is not prime")

    print("Primes up to", number, ":", find_primes(number))


if __name__ == "__main__":
    main()
