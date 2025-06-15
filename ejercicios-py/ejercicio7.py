import random

palabras = ["Hola", "Python", "Javascript", "OpenAI", "Inteligencia"]
palabra = random.choice(palabras)
inversa = palabra[::-1]  # Invierte la cadena

print(f"{palabra} -> {inversa}")