var today = new Date
    hours = today.getHours()
    month = today.getMonth()
    year = today.getFullYear()
    day = today.getDay()
    dayName = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];

function obtainDate (){
  if (hours > 12) {
    hours -= 12
    return hours + " PM"
  }else if (hours == 0) {
     return hours + " AM"
  }else return hours + "AM"
}
console.log("Today is " + dayName[day])
console.log("Current time is " + obtainDate() + ":" + today.getMinutes())
