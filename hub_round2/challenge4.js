let word1 = "dad";
let wor2 = "calculator";
let word3 = "level";
let word4 = "racecar";
let word5 = "python";

function isPalindrome(str) {
  let reversed = str.split("").reverse().join("");
  if (reversed === str) {
    return true;
  } else {
    return false;
  }
}

let palindromeCheck1 = isPalindrome(word1);
let palindromeCheck2 = isPalindrome(wor2);
let palindromeCheck3 = isPalindrome(word3);
let palindromeCheck4 = isPalindrome(word4);
let palindromeCheck5 = isPalindrome(word5);

console.log(palindromeCheck1);
console.log(palindromeCheck2);
console.log(palindromeCheck3);
console.log(palindromeCheck4);
console.log(palindromeCheck5);
