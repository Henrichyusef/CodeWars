"""
In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2
"""

def digital_root(n):

    #It creates a list with all numbers inside the given N
    digitalroot = [int(i) for i in str(n)]

    #Summation of all numbers inside the list, used as a count variable for the while loop
    digitalroot2 = int(sum(digitalroot))

    #If the previous summation is >= 10 the loop will iterate through the N numbers and then doing a new summation to see if
    #the loop fits the criteria again.

    while digitalroot2 >= 10:
        digitalroot2 = [int(i) for i in str(digitalroot2)]
        digitalroot2 = int(sum(digitalroot2))
    return digitalroot2
