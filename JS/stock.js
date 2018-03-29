// function priceGain(nums) {
//     var buyDifference = []
//         //  var maxDifference = 
//     for (i = 1; i < nums.length; i++) {
//         buyDifference.push(nums[i] - nums[i - 1])
//     }
//     return Math.max(...buyDifference)
// }

// console.log(priceGain([0, 11, 5, 9, 14, 12, 3]))

function priceGain(nums) {
    var buyDifference = null
    for (i = 1; i < nums.length; console.log(priceGain([0, 11, 5, 9, 14, 12, 3])) i++) {
        if (nums[i] - nums[i - 1] > buyDifference) {
            buyDifference = nums[i] - nums[i - 1]
        }
    }
    return buyDifference
}
console.log(priceGain([0, 11, 5, 9, 14, 12, 3]))