let form = document.querySelector("form");

form.addEventListener("submit", function (e) {
  e.preventDefault();
  console.log("the button is being clicked! again again ");
});

let input = document.querySelector("form input")

let guess = input.value

async function getGuess() {
    let res = await axios.post('/guess', )
}

