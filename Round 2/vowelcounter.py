#Challenge 3: Vowel Counter

#Description: Given a string, return the count of vowels (a, e, i, o, u) present in the string. The function should be case-insensitive (count both uppercase and lowercase vowels).

#Tests:

#countVowels("hello") should return 2.

#countVowels("why") should return 0.

#countVowels("AEIOU") should return 5.

#countVowels("JavaScript") should return 3.

#countVowels("The weather is nice today") should return 9.



def countVowels(word):
    vowels = "aeiouAEIOU"
    vowels_count = 0

    for char in word:  
        if char in vowels:  
            vowels_count += 1
    return vowels_count  

input_word = input("Enter a word: ")
vowel_count = countVowels(input_word)
print(f"The word '{input_word}' contains {vowel_count} vowels.")
