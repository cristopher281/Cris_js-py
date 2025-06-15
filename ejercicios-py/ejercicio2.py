# Generar una lista de 10 números aleatorios entre 1 y 100
import random
numeros = [random.randint(1, 100) for _ in range(10)]

# Filtrar los números pares
pares = [n for n in numeros if n % 2 == 0]

# Filtrar los números impares
impares = [n for n in numeros if n % 2 != 0]

# Mostrar los resultados en la consola
print(f"Números: {numeros}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")