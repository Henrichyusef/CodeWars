"""
Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)

Example:

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
"""
def sum_array(arr):
    if arr == None:
        return 0
    if len(arr) == 0: 
        return 0 
    if len(arr) == 1:
        return 0
    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr)
    
