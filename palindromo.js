#!/usr/bin/node
// function that returns if the word is palindrome
let word = prompt("Ingrese una palabra:");

// is converted to lowercase
word = word.toLowerCase(); 

let wordBackwards = "";

// go through the word backwards
for (let i = word.length - 1; i >= 0; i--) {
  wordBackwards += word[i];
}

if (word === wordBackwards) {
  console.log(word + " is an palíndrome");
} else {
  console.log(word + " is an palíndrome");
}