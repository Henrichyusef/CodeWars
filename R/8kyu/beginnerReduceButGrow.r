#Given a non-empty array of integers, 
#return the result of multiplying the 
#values together in order. Example:

#[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24


grow <- function(arr) {
    ab <- 1
    for (i in arr){
        ab <- ab * i
}
  return(ab)
}

#or


grow <- function(arr) {
  Reduce("*", arr)
}