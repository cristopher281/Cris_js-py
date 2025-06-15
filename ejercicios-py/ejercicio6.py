import random

n = random.randint(1, 10)  # Genera un número aleatorio entre 1 y 10
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")