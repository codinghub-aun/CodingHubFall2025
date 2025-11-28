def isPalindrome(s):
    s = s.lower()
    return s == s[::-1]
print(isPalindrome("racecar"))  
print(isPalindrome("hello"))  
print(isPalindrome("Rotator"))  
print(isPalindrome("12321"))  
print(isPalindrome("coding"))  

