"""

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false


"""

def xo(s):

    finalX = 0
    finalO = 0
    
    for i in s:
        if i == 'x':
            finalX += 1
        elif i == 'X':
            finalX += 1
        elif i == 'o':
            finalO += 1
        elif i == 'O':
            finalO += 1

    return finalX == finalO

#it counts the number of X and O (case insensitive) and returns a boolean value
