def getlongestword(sentence):
    text = sentence.split()
    return max(len(word) for word in text)

print(getlongestword("The quick brown fox"))  
print(getlongestword("Hello world"))
print(getlongestword("I love coding"))
print(getlongestword("A"))
print(getlongestword("Supercalifragilisticexpialidocious is long"))
