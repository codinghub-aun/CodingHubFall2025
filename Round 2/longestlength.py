#Challenge #2: Find the Longest Word

#Description: Given a sentence string, return the length of the longest word. Assume words are separated by single spaces.

#Tests:

#findLongestLength("The quick brown fox") should return 5. (Explanation: "quick" or "brown")

#findLongestLength("Hello world") should return 5.

#findLongestLength("I love coding") should return 6. (Explanation: "coding")

#findLongestLength("A") should return 1.

#findLongestLength("Supercalifragilisticexpialidocious is long") should return 34.

def findLongestLength(input_string):
    def length_of_longest_word(sentence):
        words = sentence.split(' ') 
        max_length = 0 
        if len(word) > max_length:
                max_length = len(word) 
        return max_length

    sentence = "The quick brown fox"
    print(f"find Longest Length '{sentence}' is: {max_length(sentence)}")

    sentence1 = "Hello World"
    print(f"Longest Lengthed word '{sentence1}' is: {length_of_longest_word(sentence1)}")

    
    sentence2 = "I love coding"
    print(f"find Longest Length '{sentence2}' is: {length_of_longest_word(sentence2)}")


    sentence = "A"
    print(f"find Longest Length '{sentence3}' is: {length_of_longest_word(sentence3)}")


    sentence = "Supercalifragilisticexpialidocious is long"
    print(f"find Longest Length '{sentence4}' is: {length_of_longest_word(sentence4)}")


    
