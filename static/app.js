//Grab the form
let form = document.getElementById("form");
//Grab the total score
let total = document.getElementById("score");
//Grab the high score
let highscore = document.getElementById("highscore");
//Grab the number of amount times played
let playedTimes = document.getElementById("times-played");

//Initialize score of 0 at the beginning of the game
let score = 0;
//Update the interface to represent the score
total.innerHTML = score;

async function handleSubmit(e) {
  //Prevents refresh of page
  e.preventDefault();
  //Grab Guess from the input value
  let guess = document.getElementById("guess").value;
  console.log("Guess:", guess);
  //Request a response to our FLASK server
  let response = await axios.get("/guess", { params: { guess: guess } });
  console.log("Response:", response);
  //Store that response
  result = response.data.result;
  console.log("Result:", result);
  //If the word is valid, tell the user
  if (result === "ok") {
    alert("Valid word!");
    score += guess.length;
    total.innerHTML = "Score: " + score;
    console.log("Score: ", score);
  }
  //If the word is not-on-board, tell the user
  else if (result === "not-on-board") {
    alert("Word is not on the board");
  }
  //If the word is not-word, tell the user
  else if (result === "not-word") {
    alert("Not a valid word");
  }
  //Reset the input value when you submit/guess a word
  guess = "";
}

async function gameOver() {
  //Change the innerHTML of score to a actually integer instead of string
  let scoreText = total.innerHTML.replace("Score ", "");
  let score = parseInt(scoreText);

  //Send to server
  let response = await axios.post("/game-over", { score: score });

  //Display Highscore/Amount of times played
  highscore.innerHTML = "Highscore: " + response.data.highscore;
  playedTimes.innerHTML = "You have played " + response.data.played + " times";

  console.log(response);
}

//60 Second Timer
function handleTimer() {
  alert("Time is up! Game over");
  guess.disabled = true;
  gameOver();
}

let timer = setTimeout(handleTimer, 60000);

//Submit the word/form
form.addEventListener("submit", handleSubmit);
