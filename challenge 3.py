def countvowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)

print(countvowels("hello")) 
print(countvowels("why")) 
print(countvowels("AEIOU")) 
print(countvowels("JavaScript")) 
print(countvowels("The weather is nice today"))  
