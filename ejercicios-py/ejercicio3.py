import random

palabras = ["Aceituna", "Murciélago", "Educación", "Aeropuerto", "Otorrinolaringólogo", "Euforia", "Aceite", "Paleontólogo", "Arquitectura", "Hipopótamo"]
palabra = random.choice(palabras)
vocales = [c for c in palabra.lower() if c in "aeiouáéíóú"]
print(f"Palabra: {palabra}")
print(f"Vocales: {', '.join(vocales)}")
print(f"Total de vocales: {len(vocales)}")