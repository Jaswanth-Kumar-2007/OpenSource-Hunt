def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error"  # Should raise exception or handle better
    return a / b


def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", multiply(a, b))
    elif choice == "3":
        print("Result:", subtract(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    calculator()
#akilan
