"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
"""
import math
def find_next_square(sq):
    """ Finds the next perfect square """
    sqrtOfSq = int(math.sqrt(sq))
    #int() will help to filter the non perfect squares
    confirmPrfct = sqrtOfSq ** 2
    if confirmPrfct == sq:
        nextPrfct = confirmPrfct + 1
        while True:
            sqrtOfnextPrfct = int(math.sqrt(nextPrfct))
            if sqrtOfnextPrfct ** 2 == nextPrfct:
                return nextPrfct
            else:
                nextPrfct += 1
    return -1

print(find_next_square(25))

