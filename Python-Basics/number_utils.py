def is_even(number):
    return number % 2 == 0


def find_max(numbers):
    if not numbers:
        return None

    maximum = numbers[0]

    for number in numbers:
        if number < maximum:  # Bug: this finds minimum, not maximum
            maximum = number

    return maximum


def find_min(numbers):
    if not numbers:
        return None

    minimum = numbers[0]

    for number in numbers:
        if number > minimum:
            minimum = number

    return minimum


def calculate_sum(numbers):
    total = 0

    for number in numbers:
        if not isinstance(number, int):
            raise TypeError("Only integers are allowed")

        total += number

    return total


if __name__ == "__main__":
    numbers = [10, 25, 7, 42, 18]

    print("Numbers:", numbers)
    print("Maximum:", find_max(numbers))
    print("Minimum:", find_min(numbers))
    print("Sum:", calculate_sum(numbers))
