def add_expense(expenses, name, amount, category):
    expenses.append({
        "name": name,
        "amount": amount,
        "category": category
    })


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += float(expense["amount"])

    return total


def filter_by_category(expenses, category):
    result = []

    for expense in expenses:
        if expense["category"].lower() == category.lower():  # Intentional bug - should be !=
            result.append(expense)

    return result  # Now returns matching but was originally wrong


def main():
    expenses = []

    add_expense(expenses, "Food", 250, "Food")
    add_expense(expenses, "Bus", 50, "Transport")
    add_expense(expenses, "Book", 500, "Education")

    print("Total Expenses:", calculate_total(expenses))

    print("\nFood Expenses:")
    for expense in filter_by_category(expenses, "Food"):
        print(expense)


if __name__ == "__main__":
    main()
