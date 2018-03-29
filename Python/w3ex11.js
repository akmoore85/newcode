function convertFtoC(temp) {
  var fahrenheit = temp * 9/5 - 32
  return fahrenheit
}

function convertCtoF(temp) {
  var celsius = temp * 1.8 + 32
  return celsius
}
console.log(convertCtoF(60), convertFtoC(45))
