import random

longitud = random.randint(16, 40)
caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
contraseña = "".join(random.choice(caracteres) for _ in range(longitud))

print(f"Contraseña generada ({longitud}): {contraseña}")