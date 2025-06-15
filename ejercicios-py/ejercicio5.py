import random

secreto = random.randint(1, 100)
while True:
    intento = random.randint(1, 100)
    if intento < secreto:
        print(f"{intento} es menor ❌")
    elif intento > secreto:
        print(f"{intento} es mayor ❌")
    else:
        break
print(f"¡Correcto! El número era {secreto} ✅")