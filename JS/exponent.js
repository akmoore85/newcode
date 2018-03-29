function exponent(base, exp) {
    if (exp == 0) {
        return 1
    } else if (exp == 1) {
        return base
    } else {
        return base * exponent(base, exp - 1)
    }
}
console.log(exponent(5, 4))