\\ Rock , Paper , Scissors game in Javascript
choices = ["rock", "paper", "scissors"]
let player_choice = prompt("Enter your choice: rock, paper, or scissors").toLowerCase();
var random_choice = {
    1: "rock",
    2: "scissors",
    3: "paper"
}
let random_num = random_choice[Math.floor(Math.random() * 3) + 1];
let computer_choice = random_choice[random_num];
console.log("Computer choice :" + computer_choice);
console.log("Player choice: " + player_choice);
if(player_choice === computer_choice){
    alert("It's a tie!");
}else if(player_choice === "rock"&& computer_choice === "scissors") {
    alert("You win!");
}else if(player_choice === "paper"&& computer_choice === "rock") {
    alert("You win!");
}else if(player_choice === "scissors" && computer_choice === "paper") {
    alert("You win!");
}else{
    alert("Computer wins!");
}
