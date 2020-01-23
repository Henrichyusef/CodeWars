"""
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) 
and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. 
When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll 
have to capitalize each word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. 
The strings are actual quotes from Jaden Smith, but they are not capitalized in the same 
way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
"""
def toJadenCase(string):
    words = string.lower().split()
    phrase = ''
    for i in words:
        phrase += i[0].upper() + i[1:] + ' '
    return phrase.strip()

#using join
def toJadenCase3(string):
    words = string.split()
    wordsJaden = [i[0].upper() + i[1:] for i in words]
    return ' '.join(wordsJaden)


# absolutely not a bestpractice thing but it's a genius one
from string import capwords as cap

#using string module
from string import capwords

def toJadenCase2(string):
    return capwords(string)
