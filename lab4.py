def format_price(price):
    return f"ціна: {price:.2f} грн"
def available_products(*items):
    store = {
        "хліб": True,
        "молоко": True,
        "яйця": False,
        "цукор": True,
        "сіль": True
    }
    return {item: store.get(item, False) for item in items}
def make_order(order, prices, available, action="купити"):
    if not all(available.get(item, False) for item in order):
        return "Замовлення неможливе: деякі товари відсутні."
    total = sum(prices.get(item, 0) for item in order)

    if action == "переглянути":
        return f"Загальна {format_price(total)}"
    elif action == "купити":
        return f"Ви успішно купили товари на {format_price(total)}"
    else:
        return "Невідома дія"
prices = {
    "хліб": 25,
    "молоко": 30,
    "яйця": 60,
    "цукор": 40,
    "сіль": 15
}
order = ["молоко", "сіль", "цукор"]
available = available_products(*order)
print(make_order(order, prices, available, "переглянути"))
print(make_order(order, prices, available, "купити"))