STORE_INVENTORY = {
    "молоко": (True, 35.50),
    "хліб": (True, 22.00),
    "сир": (False, 180.99),
    "йогурт": (True, 25.00),
    "ковбаса": (False, 250.00),
    "кава": (True, 150.75),
}

def format_price(price):
    return f"Ціна: {price:.2f} грн"
def check_availability(items_list):
    return {
        item: STORE_INVENTORY.get(item.lower(), (False, 0))[0]
        for item in items_list
    }
def process_order(items_list, action):
    availability = check_availability(items_list)
    if not all(availability.values()):
        return (f"Замовлення неможливе. Відсутні товари або невідомі товари")
    total_price = sum(STORE_INVENTORY[item.lower()][1] for item in items_list)
    if action.lower() == 'переглянути':
        return f"Загальна ціна: {format_price(total_price)}."
    elif action.lower() == 'купити':
        return f"Дякуємо! Замовлення оформлено. Сума: {format_price(total_price)}."
if __name__ == "__main__":
    print("Ласкаво просимо до магазину!")
    while True:
        user_input_item = input("Введіть товари через кому: ")
        order_list = [item for item in user_input_item.split(',')]
        action = input("Ваша дія ('купити' або 'переглянути', або 'вихід'): ")
        if action.lower() == 'вихід':
            print("Дякуємо за використання! До побачення.")
            break
        result = process_order(order_list, action)
        print(result)
        break
