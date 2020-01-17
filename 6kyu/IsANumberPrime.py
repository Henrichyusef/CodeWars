"""
Define a function that takes an integer argument and returns logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Example

is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */

Assumptions

    You can assume you will be given an integer input.
    You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
    There are no fancy optimizations required, but still the most trivial solutions might time out. Try to find a solution which does not loop all the way up to n.
"""

import math
def is_prime(x):
    if x <= 3:
        return x >= 2
    if x > 2 and x % 2 == 0:
        return False
    number = math.floor(math.sqrt(x))
    for i in range(3, number+1, 2):
        if x % i == 0:
            return False
    return True
