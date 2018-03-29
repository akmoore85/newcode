function isPalindrome(word) {
    var lower = word.toLowerCase()
    for (i = 0; i = lower.length; i++) {
        console.log(lower[i])
        if (i == lower[i].length - 1) {
            console.log(i)
            return "Okay so far"
        } else return "Not a Palindrome"

    }
}
console.log(isPalindrome("hannah"))