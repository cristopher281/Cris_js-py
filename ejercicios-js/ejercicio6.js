const n = Math.floor(Math.random() * 10) + 1;
let factorial = 1;
for (let i = 1; i <= n; i++) {
  factorial *= i;
}
console.log(`${n}! = ${factorial}`);