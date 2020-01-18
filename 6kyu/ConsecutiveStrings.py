#The original kata explanation was incomprehensible
"""
Explanation by user Tigerdevon:

I couldn't figure out what the instructions were trying to say, and, it seemed that tons of other people were having the same problem lol
I finally figured out what they were trying to say and decided that I should try to help others understand it :)
I'm gonna reword the instructions so they'll hopefully make sense to more people. (Also, the code is gonna be python 3 because that's what I'm learning)

def longest_consec(str_arr, k):
    #Your code here

Goal: Make the longest string using k(int) amount of (consecutive) strings from the array(str_arr)

Example:

longest_consec(["it","wkppv","ixoyx", "3452", "zzz4zzzz9zzz"], 3)

The three options:

1) [0]"it"    [1]"wkppv" [2]"ixoyx"        ; "itwkppvixoyx"
2) [1]"wkppv" [2]"ixoyx" [3]"3452"         ; "wkppvixoyx3452"
3) [2]"ixoyx" [3]"3452"  [4]"zzz4zzzz9zzz" ; "ixoyx3452zzz4zzzz9zzz"

k(int) is the reason why there are 3 strings per answer

The answer is:

3) "ixoyx3452zzz4zzzz9zzz"

Because it's the longest! (If there are multiple options with the same length of string, then you use the first of those options)
I hope this helps someone!
"""
words = ["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"]
k = 2
