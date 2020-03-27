"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.

"""
def solution(number):
    a = 3
    b = 5

    #this part separates the multiples of 3 from the rest of the numbers.
    list3 = []
    for i in range(1, number, 1):
        if i%a == 0:
            list3.append(i)

    #this part separates the multiples of 5 from the rest of the numbers.
    list5 = []
    for i in range(1, number, 1):
        if i%b == 0:
            list5.append(i)

    #this part compares if there is any repeted numbers and allocate them altogether.
    for i in list3:
        if i not in list5:
            list5.append(i)
            
    return sum(list5)
