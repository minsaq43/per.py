\\ variable swapping program
var a = prompt("Enter a number: ");
var b = prompt("Enter other number: ");
console.log(`now the value of a and b is ${a} and ${b}`);
var temp ;
temp = a;
a = b;
b = temp;
console.log(`Then the value of a and b is ${a} and ${b}`);
