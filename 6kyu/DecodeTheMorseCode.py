"""
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superceded by voice and digital data communication channels, it still has its use in some applications around the world.

The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−− ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

--- In this solution the dictionary was added even though it's not necessary as the kata provides it --
"""
def decodeMorse(morse_code):
    morse_code1 = {'A':'.-', 'B':'-...',
                  'C':'-.-.', 'D':'-..', 'E':'.',
                  'F':'..-.', 'G':'--.', 'H':'....',
                  'I':'..', 'J':'.---', 'K':'-.-',
                  'L':'.-..', 'M':'--', 'N':'-.',
                  'O':'---', 'P':'.--.', 'Q':'--.-',
                  'R':'.-.', 'S':'...', 'T':'-',
                  'U':'..-', 'V':'...-', 'W':'.--',
                  'X':'-..-', 'Y':'-.--', 'Z':'--..',
                  '1':'.----', '2':'..---', '3':'...--',
                  '4':'....-', '5':'.....', '6':'-....',
                  '7':'--...', '8':'---..', '9':'----.',
                  '0':'-----', ',':'--..--', '.':'.-.-.-',
                  '?':'..--..', '/':'-..-.', '-':'-....-',
                  '(':'-.--.', ')':'-.--.-', 'SOS':'...---...',
                  '!':'-.-.--'}
    morse_code2 = {i:j for j, i in morse_code1.items()} #converts the values to keys
    morse_code += ' ' 
    #adds white space to the final so the last letter can be deciphered
    
    morse_code = morse_code.lstrip()
        #removes all white spaces from the beginning
    
    decipher = ''
    morse1 = ''
    i = 0
    for symbol in morse_code:
        if symbol != ' ':
            i = 0 
            #counter to keep track of spaces
            morse1 += symbol
        else:
            i += 1 
            #if i == 1 morse1 will be converted to a letter and then cleared
            if i >= 2: 
            #if i > 2, it will be converted to space when it reaches 3
                if i == 3:
                    decipher += ' '
            else:
                decipher += morse_code2[morse1]
                morse1 = ''
                #strip removes all white spaces from the start and end
    return decipher.strip()
