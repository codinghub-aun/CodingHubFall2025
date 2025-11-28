let word1 = "hello";
let word2 = "world";
let word3 = "javascript";
let word4 = "programming";
let word5 = "developer";
function reverseString(str) {
  return str.split("").reverse().join("");
}

let reversedWord1 = reverseString(word1);
let reversedWord2 = reverseString(word2);
let reversedWord3 = reverseString(word3);
let reversedWord4 = reverseString(word4);
let reversedWord5 = reverseString(word5);

console.log(reversedWord1);
console.log(reversedWord2);
console.log(reversedWord3);
console.log(reversedWord4);
console.log(reversedWord5);
