const numeros = Array.from({ length: 10 }, () => Math.floor(Math.random() * 50) + 1);
const suma = numeros.reduce((acc, val) => acc + val, 0);

console.log(`Números aleatorios: ${numeros}`);
console.log(`Suma total: ${suma}`);