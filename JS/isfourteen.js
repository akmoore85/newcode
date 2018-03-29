function isFourteen(num) {
    sets = []
    target = 14
    for (i = 0; i < num.length; i++) {
        console.log('this is the first step' + num[i])
        for (j = 0; j < num.length; j++) {
            if (num[i] + num[j] == target) {
                sets.push([num[i], num[j]])
            }
        }
    }
    return sets
}

console.log(isFourteen([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))