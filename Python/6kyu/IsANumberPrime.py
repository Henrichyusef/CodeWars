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
import time
import math

#V1 = 107.71 seconds, testing all primes from 1 to 100.000
#V2 = 14.2 seconds, testing all primes from 1 to 100.000

## FIRST VERSION ## TESTS ALL NUMBERS FROM 2 UP TO X ONE BY ONE.
"""
def is_prime(x):
    if x <= 3:
        return x >= 2
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

t0 = time.time()
for j in range (1, 100000):
    print(j, is_prime(j))
t1 = time.time()
print('Time required:', t1-t0)
"""

## SECOND VERSION ## IT TESTS ALL NUMBER FROM 2 UP TO SQUARE OF X, SINCE EVERYTHING ABOVE WILL REPEAT ITSELF BASICALLY.
"""
def is_prime(x):
    if x <= 3:
        return x >= 2
    number = math.floor(math.sqrt(x))
    for i in range(2, number + 1):
        if x % i == 0:
            return False
    return True
t0 = time.time()
for i in range (1, 100000):
    print(i, is_prime(i))
t1 = time.time()

print("Time required: ", t1-t0)
"""
## THID VERSION ## IT TESTS ONLY ODD NUMBERS SINCE EVEN NUMBERS BESIDES 2 CANNOT BE PRIMES USING THE SECOND VERSION METHOD.

def is_prime(x):
    #eliminates numbers <= 3
    if x <= 3:
        return x >= 2
    #eliminates all even numbers
    if x > 2 and x % 2 == 0:
        return False
        
    #check only odd numbers up to the sqrt of x
    number = math.floor(math.sqrt(x))
    for i in range(3, number+1, 2):
        if x % i == 0:
            return False
    return True

t0 = time.time()
for j in range(1, 10):
    print(j, is_prime(j))
t1 = time.time()
print("Required time: ", t1 - t0)