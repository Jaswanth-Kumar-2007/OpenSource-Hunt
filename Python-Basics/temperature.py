def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice: ")

    try:
        temperature = float(input("Enter temperature: "))
    except ValueError:
        print("Invalid temperature")
        return

    if choice == "1":
        print("Result:", celsius_to_fahrenheit(temperature))
    elif choice == "2":
        print("Result:", fahrenheit_to_celsius(temperature))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()