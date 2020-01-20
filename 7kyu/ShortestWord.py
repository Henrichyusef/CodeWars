"""
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.

"""
def find_short(s):
    lenOfWords = []
    words = []
    s += ' '
    word = ''
    for i in s:
        if i == ' ':
            words.append(word.strip())
            lenOfWords.append(len(word.strip()))
            word = ''
        word += i
    return min(lenOfWords)


