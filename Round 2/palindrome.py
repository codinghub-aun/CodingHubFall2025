#Challenge 4: Palindrome Checker

#Description: Given a string, return true if the string is a palindrome (reads the same forwards and backwards) and false otherwise. Note: For this challenge, assume inputs are single words without spaces or special characters, but case should be ignored (e.g., "Mom" is a palindrome).

#Tests:

#isPalindrome("racecar") should return true.

#isPalindrome("hello") should return false.

#isPalindrome("Rotator") should return true.

#isPalindrome("12321") should return true.

#isPalindrome("coding") should return false.

def isPalindrome(word):
    cleaned_word = word.lower().replace(" ", "") 
  
  
    return cleaned_word == cleaned_word[::-1]

# Example usage:
print(isPalindrome("racecar"))
print(isPalindrome("hello")) 
print(isPalindrome("rotator"))
print(isPalindrome("123321"))
print(isPalindrome("coding"))
