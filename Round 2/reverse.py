#Challenge #1: String Reversal

#Description: Given a string, return a new string with the characters in reverse order.

#Tests:

#reverseString("hello") should return "olleh".

#reverseString("Python") should return "nohtyP".

#reverseString("12345") should return "54321".

#reverseString("racecar") should return "racecar".

#reverseString(" A B C ") should return " C B A ".

def reversestring(input_string):
  return input_string[::-1]

print(f"reversestring(\"Python\") should return: {reversestring('Python')}")
print(f"reversestring(\"hello\") should return: {reversestring('hello')}")
print(f"reversestring(\"12345\") should return: {reversestring('12345')}")
print(f"reversestring(\"racecar\") should return: {reversestring('racecar')}")
print(f"reversestring(\" A B C \") should return: {reversestring(' A B C ')}")
