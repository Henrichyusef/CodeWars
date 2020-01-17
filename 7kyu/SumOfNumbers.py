"""
Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples

get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

"""

def get_sum(a,b):
#this section compares if a equals to b, if so, it will return a.
    if a == b: 
        return a
#this section will be applied when a is greater than b thus the for loop needs to count backwards.
    elif a > b: 
        sumbox1 = 0
        for i in range(a, b-1, -1):
            sumbox1 += i
        return sumbox1
#this section sums the numbers between a and b, when b is greater than a.
    else:
        sumbox = 0
        for i in range(a, b+1, 1):
            sumbox += i
        return sumbox
