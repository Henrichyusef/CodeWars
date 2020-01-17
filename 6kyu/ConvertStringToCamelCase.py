"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
Examples

to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

"""
def to_camel_case(text):
    
    text = text.replace('-', ' ')
    text = text.replace('_', ' ') + ' '

    word = ''
    text1 = ''
    count = 0
    for i in text:
        if i == ' ':
            count += 1
            if count > 1:
                text1 += word[0].upper() + word[1:]
                word = ''
            else:
                text1 += word
                word = ''
        else:
            word += i
    return text1.strip()
