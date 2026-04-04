let words = [];
let game_over = false;
function playWord(word) {
  word = word.toLowerCase();
  if (game_over) return "game over";
  if (words.includes(word)) {
    game_over = true;
    return "game over";
  }
  if (words.length > 0 && word[0] !== words[words.length - 1].slice(-1)) {
    game_over = true;
    return "game over";
  }
  words.push(word);
  return words;
}
function restartGame() {
  words = [];
  game_over = false;
  return "game restarted";
}
while (!game_over) {
  let input = prompt("Enter a word:");
  if (input === null) break;
  let result = playWord(input);
  alert(result);
}
alert("Game over! Words used: " + words.join(", "));