""" You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)
Examples

[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3 

"""

def stray(arr):
    minValue = min(arr)
    maxValue = max(arr)

    countMax = []
    countMin = []
    for i in arr:
        if i == minValue:
            countMin.append(i)
        else:
            countMax.append(i)
    return minValue if len(countMax) > len(countMin) else maxValue

#another solution

def stray1(arr):
    return [i for i in arr if arr.count(i) == 1][0]


