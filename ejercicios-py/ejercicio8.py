import random

numeros = []
for _ in range(10):
    numeros.append(random.randint(1, 50))

suma = 0
for num in numeros:
    suma += num

print(f"Números aleatorios: {numeros}")
print(f"Suma total: {suma}")