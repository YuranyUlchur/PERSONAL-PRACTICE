#!/usr/bin/node
// function add an item to the list, removes it, and returns it
function nextInTheFile (list, element) {
  for (let i = 0; i <= element.length - 1; i++) {
    list.push(element[i]);
  }// add an element at the end
  return list.shift();// remove first element
}

let myList = [1, 2, 3, 4, 5, 6, 7];
// converts the object into a string
// print of myList
console.log('BEFORE' + JSON.stringify(myList));
// element add
console.log(nextInTheFile(myList, [8, 9, 10, 50, 12, 80]));
// print myList new
console.log('AFTER' + JSON.stringify(myList));
