def pendulum(values):
    """Sort numbers into a pendulum order"""
    values.sort()
    # 1 = right 0 = left
    rightOrLeft = 1
    minValue = min(values)

    leftList = []
    rightList = [minValue]

    for number in values[1:]:
        if rightOrLeft == 1:
            rightList.append(number)
            rightOrLeft = 0
        else:
            leftList.append(number)
            rightOrLeft = 1
    return leftList[::-1] + rightList

print(pendulum([6, 6, 8 ,5 ,10]))