#You are given two angles (in degrees) of a triangle.
#Write a function to return the 3rd.
#Note: only positive integers will be tested.


other_angle <- function(a, b){
  return( abs(180 - (a + b)) )
}