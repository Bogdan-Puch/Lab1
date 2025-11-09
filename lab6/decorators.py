import time

def delay(func):
    def wrapper(*args, **kwargs):
        print("Зачекай 5 секунд...")
        time.sleep(5)   # затримка
        return func(*args, **kwargs)  # виклик оригінальної функції
    return wrapper