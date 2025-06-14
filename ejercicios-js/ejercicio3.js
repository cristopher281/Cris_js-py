const palabras = ["Aceituna", "Murciélago", "Educación", "Aeropuerto", "Otorrinolaringólogo", "Euforia", "Aceite", "Paleontólogo", "Arquitectura", "Hipopótamo"];
const palabra = palabras[Math.floor(Math.random() * palabras.length)];
const vocales = palabra.toLowerCase().split('').filter(c => "aeiouáéíóú".includes(c));
console.log(`Palabra: ${palabra}`);
console.log(`Vocales: ${vocales.join(", ")}`);
console.log(`Total de vocales: ${vocales.length}`);