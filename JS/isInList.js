function isInList(array, item) {
  for (i = 0; i < array.length(); i++){
    if (array[i] == item) {
      return true
    }
  }return false
}

arr = [{'name':'secada', 'name':'joel', 'name':'good1', 'name':'clapton'}]

function numberName(array){
  for (i = 0; i < array.length; i++){
    console.log(array[i].name)
  }
}
console.log(numberName(arr))
