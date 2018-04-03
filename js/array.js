console.log([...Array(12).keys()].map(i => i + 1));

const a1 = [1, 2, 3];
console.log(a1.unshift(4));
console.log(a1);
console.log(a1.push(6));
console.log(a1);
console.log(a1.pop());
console.log(a1.pop());
console.log(a1);

console.log(null || [])
console.log(undefined || [])


const a2 = [...Array(5).keys()];
console.log(a2.filter((v) => v > 2).map((v) => v * 2));
console.log(a2.some((v) => v > 3));
console.log(a2.find((v) => v > 2)); //essential find one
console.log(a2.every((v) => v < 10));
console.log(a2.every((v) => v > 3));
a2.reverse().forEach((v, i) => { console.log(`${i} --> ${v}`); })

const animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];
console.log(animals.slice(2, 4));
console.log(animals.slice(2));
