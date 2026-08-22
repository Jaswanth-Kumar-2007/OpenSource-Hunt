def calculate_subtotal(cart):
    total = 0

    for item in cart:
        total += item["price"]

    return total


def calculate_discount(total):
    if total >= 1000:
        return total * 0.20
    elif total >= 500:
        return total * 0.10

    return 0


def calculate_total(cart):
    subtotal = calculate_subtotal(cart)
    discount = calculate_discount(subtotal)

    return subtotal - discount


def add_item(cart, name, price, quantity):
    cart.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })


def main():
    cart = []

    add_item(cart, "Notebook", 100, 2)
    add_item(cart, "Pen", 20, 5)
    add_item(cart, "Bag", 800, 1)

    print("Shopping Cart")
    print("-------------")

    for item in cart:
        print(
            item["name"],
            "- ₹",
            item["price"],
            "x",
            item["quantity"]
        )

    print("Total:", calculate_total(cart))


if __name__ == "__main__":
    main()
