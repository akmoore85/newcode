function letterRoll(word) {
  var newString = word.split('')
  setInterval(function(){
    var backLetter = newString.pop()
    newString.unshift(backLetter)
    console.log(newString.join())
   }, 3000);
}
letterRoll("thesis")
