from decorators import delay

@delay
def hello(name):
    print(f"Привіт, {name}!")
hello("Друже")