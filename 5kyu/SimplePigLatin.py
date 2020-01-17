"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    alphabet = ["n", "m", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

    user = text + ' '
    finaltext = ''
    word = ''
    for i in user:
        if i == ' ':
            if word[-1].lower() in alphabet: 
                finaltext += word[1:] + word[0] + 'ay' + ' '
                word = ''
            else:
                if len(word) == 1:
                    finaltext += word + ' '
                else:    
                    finaltext += word[1:-1] + word[0] + 'ay' + word[-1] + ' '
                    word = ''
        else:
            word += i
    return finaltext.strip()
