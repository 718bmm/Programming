var playerScore = 0;
var computerScore = 0;
var round = 0;

function playRound() {
    var playerGuess = parseInt(document.getElementById("playerGuess").value);
    var computerGuess = Math.floor(Math.random() * 10) + 1;
    
    var playerDifference = Math.abs(playerGuess - computerGuess);
    
    round++;
    document.getElementById("round").innerHTML = "Round" + " " + round
    document.getElementById("result-cg").innerHTML = computerGuess;
    document.getElementById("result-pg").innerHTML = playerGuess;
    
    

    if (playerDifference === 0) {
        document.getElementById("result").innerHTML += "It's a tie!";
    } else if (playerDifference <= 2) {
        playerScore++;
        document.getElementById("score-pg").innerHTML += 1;
        document.getElementById("result-pg").innerHTML += "<br>You win!";
    } else {
        computerScore++;
        document.getElementById("score-cg").innerHTML += 1;
        document.getElementById("result-cg").innerHTML += "<br>Computer wins!";
    }
    
    if (round === 3) {
        endGame();
    }
}

function endGame() {
    document.getElementById("result").innerHTML += "<br>Game Over! <br>Player Score: " + playerScore + "<br>Computer Score: " + computerScore;
    document.getElementById("btn").disabled = false;
}
