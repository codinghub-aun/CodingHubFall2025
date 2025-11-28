let sen1 = "The COLD NeVer BotherS Me";
let sen2 = "STANDING ON THE SHOULDERs OF GIANTS";
let sen3 = "to be or NOT to BE";

function toTitleCase(str) {
  let words = str.toLowerCase().split(" ");
  for (let i = 0; i < words.length; i++) {
    words[i] = words[i].charAt(0).toUpperCase() + words[i].slice(1);
  }
  return words.join(" ");
}

let titleCaseSen1 = toTitleCase(sen1);
let titleCaseSen2 = toTitleCase(sen2);
let titleCaseSen3 = toTitleCase(sen3);

console.log(titleCaseSen1);
console.log(titleCaseSen2);
console.log(titleCaseSen3);
