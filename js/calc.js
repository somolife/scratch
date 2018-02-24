const op = (fn, elems, start) => {
    return elems
        .map(i => parseInt(i))
        .reduce(fn, start);
}

const eval = (expr) => {
    elems = expr.split(' ');

    if (elems.length < 1) {
        throw 'bad input';
    } else if (elems.length == 1) {
        return parseInt(expr);
    } else {
        fn = elems.splice(0, 1)[0]
        switch (fn) {
            case '+':
                return op((x, y) => x + y, elems, 0)
            case '*':
                return op((x, y) => x * y, elems, 1)
            default:
                throw 'bad input';
        }
    }

    return null;
}

function print(s) {
    console.log(s);
}

function assert(l, r) {
    condition = () => l === r;
    if (!condition()) {
        throw `assert failed, expected ${l} --> got ${r}`;
    }
}
function test() {
    assert(1, eval("1"));
    assert(1, eval("+ 1"));
    assert(3, eval("+ 1 2"));
    assert(15, eval("+ 1 2 3 4 5"));
    assert(1, eval("* 1"));
    assert(6, eval("* 2 3"));
}

print('--- calc app ---');
test();