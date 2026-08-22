def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_lowercase(password):
    return any(char.islower() for char in password)


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_special_character(password):
    special_characters = "!@#$%^&*()"
    return any(char in special_characters for char in password)


def is_valid_password(password):
    if len(password) < 6:
        return False

    if not has_lowercase(password):
        return False

    if not has_digit(password):
        return False

    return True


def main():
    password = input("Enter password: ")

    if is_valid_password(password):
        print("Password is valid")
    else:
        print("Password is invalid")


if __name__ == "__main__":
    main()