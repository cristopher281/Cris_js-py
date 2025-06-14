const palabras = ["Hola", "Python", "Javascript", "OpenAI", "Inteligencia"];
const palabra = palabras[Math.floor(Math.random() * palabras.length)];
const inversa = palabra.split("").reverse().join("");
console.log(`${palabra} → ${inversa}`);