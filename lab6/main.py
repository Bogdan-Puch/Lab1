
from decorators import delay

@delay
def привіт(імя):
    print(f"Привіт, {імя}!")
привіт("Друже")