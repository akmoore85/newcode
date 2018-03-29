function insertDash(num) {
    var strung = num.toString().split("")
    for (i = 0; i < strung.length; i++) {
        if (i % 2 == 0) {
            strung.join('-')
        }
    }
    return strung
}

console.log(insertDash(8583890128503215))