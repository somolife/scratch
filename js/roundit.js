function precisionRound(number, precision) {
    var factor = Math.pow(10, precision);
    return (Math.trunc(number * factor) / factor).toFixed(2);
}

const check = (n) => `${n} --> ${precisionRound(n, 2)}`;

console.log(check(1234.999));
console.log(check(1234.99));
console.log(check(1234.90));
console.log(check(1234));
