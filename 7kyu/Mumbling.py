"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""

def accum(s):
    user = s.lower()
    text = ''
    length = len(user)
    for i in range(0, length):
        count = 1
        if count == 1:
            text+= user[i].upper() 
            text += user[i]*i+'-'
        
    return text[:-1]
