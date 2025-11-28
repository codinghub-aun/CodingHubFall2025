let sentence = "The quick brown fox jumps over the lazy dog";
function findlongestWord(str) {
  let words = str.split(" ");
  let longestWord = "";
  for (let word of words) {
    if (word.length > longestWord.length) {
      longestWord = word;
    }
  }
  return longestWord;
}

let longestWordInSentence = findlongestWord(sentence);
console.log(longestWordInSentence);
