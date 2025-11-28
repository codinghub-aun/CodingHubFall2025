# Challenge #1: String Reversal
#
# Description: Given a string, return a new string with the characters in reverse order.
#
# Tests:
#
# reverseString("hello") should return "olleh".
#
# reverseString("Python") should return "nohtyP".
#
# reverseString("12345") should return "54321".
#
# reverseString("racecar") should return "racecar".
#
# reverseString(" A B C ") should return " C B A ".
from operator import index

def reverseString(words):
    if len(words) == 0:
        return words
    return reverseString(words[1:]) + words[0]

print(reverseString("hello"))


