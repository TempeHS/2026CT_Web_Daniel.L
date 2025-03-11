scissors = 1;
paper = 2;
rock = 3;

player_name = prompt("Enter your name:");
alert("Hello " + player_name);

player_guess = prompt("Choose scissors, paper, or rock:").toLowerCase();

computer_guess = randomIntFromInterval(1, 3);

let computer_choice = "";
if (computer_guess === scissors) computer_choice = "scissors";
if (computer_guess === paper) computer_choice = "paper";
if (computer_guess === rock) computer_choice = "rock";

if (
  (player_guess === "scissors" && computer_guess === scissors) ||
  (player_guess === "paper" && computer_guess === paper) ||
  (player_guess === "rock" && computer_guess === rock)
) {
  document.getElementById("user_feedback").innerHTML =
    "It's a tie! Both chose " + computer_choice;
} else if (
  (player_guess === "scissors" && computer_guess === paper) ||
  (player_guess === "paper" && computer_guess === rock) ||
  (player_guess === "rock" && computer_guess === scissors)
) {
  document.getElementById("user_feedback").innerHTML =
    "You win! Computer chose " + computer_choice;
} else if (
  (player_guess === "scissors" && computer_guess === rock) ||
  (player_guess === "paper" && computer_guess === scissors) ||
  (player_guess === "rock" && computer_guess === paper)
) {
  document.getElementById("user_feedback").innerHTML =
    "You lose! Computer chose " + computer_choice;
} else {
  document.getElementById("user_feedback").innerHTML =
    "Invalid input! Please enter scissors, paper, or rock.";
}

function randomIntFromInterval(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
