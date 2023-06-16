let form = document.querySelector("form");
async function getGuess() {
  let guess = document.querySelector("#guess").value;
  let res = await axios.get("/guess", { params: { guess: guess } });
}

function handleResponse(data) {
  console.log("Server response:", data);
}
form.addEventListener("submit", function (e) {
  e.preventDefault();
  getGuess();
});
