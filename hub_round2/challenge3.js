let word1 = "hello";
let word2 = "world";
let word3 = "javascript";
let word4 = "programming";
let word5 = "developer";

function findvowelCount(str) {
  let vowels = "aeiou";
  let count = 0;
  for (let char of str) {
    if (vowels.includes(char)) {
      count++;
    }
  }
  return count;
}
findvowelCount(word1);
findvowelCount(word2);
findvowelCount(word3);
findvowelCount(word4);
findvowelCount(word5);

console.log(findvowelCount(word1));
console.log(findvowelCount(word2));
console.log(findvowelCount(word3));
console.log(findvowelCount(word4));
console.log(findvowelCount(word5));
