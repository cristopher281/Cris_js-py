const numeros = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100) + 1);

const pares = numeros.filter(n => n % 2 === 0);
const impares = numeros.filter(n => n % 2 !== 0);

console.log(`Números: ${numeros}`);
console.log(`Pares: ${pares}`);
console.log(`Impares: ${impares}`);