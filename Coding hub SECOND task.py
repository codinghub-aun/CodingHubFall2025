# Challenge #2: Find the Longest Word
# Description: Given a sentence string, return the length of the longest word. Assume words are separated by single spaces.
# Tests:
# findLongestLength("The quick brown fox") should return 5. (Explanation: "quick" or "brown")
# findLongestLength("Hello world") should return 5.
# findLongestLength("I love coding") should return 6. (Explanation: "coding")
# findLongestLength("A") should return 1.
# findLongestLength("Supercalifragilisticexpialidocious is long") should return 34.
# return max(len(word) for word in words)




def findLongestLength(sentence):
    words = sentence.split()
    return max(len(word) for word in words)

print(findLongestLength("ME THREEEE"))