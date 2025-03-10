rock = 1;
paper = 2;
scissors = 3;

player_name = prompt("enter your name");
alert("Hello " + player_name);
player_guess = prompt("rock paper scissors");
computer_guess = randomIntFromInterval(1, 3);

if (player_guess == ) {
  document.getElementById("user_feedback").innerHTML =
    "Correct, i know your cheating";
} else {
  document.getElementById("user_feedback").innerHTML =
    "You suck, the number was " + computer_guess;
}

function randomIntFromInterval(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
