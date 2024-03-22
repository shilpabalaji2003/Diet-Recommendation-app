var errors = 0;
var cardList = [
    "darkness",
    "double",
    "fairy",
    "fighting",
    "fire",
    "grass",
    "lightning",
    "metal",
    "psychic",
    "water"
]

var cardSet;
var board = [];
var rows = 4;
var columns = 5;
var confettiInterval;

var card1Selected;
var card2Selected;
var lockBoard = false;

window.onload = function() {
    shuffleCards();
    startGame();
}

function shuffleCards() {
    cardSet = cardList.concat(cardList); //two of each card
    //shuffle
    for (let i = 0; i < cardSet.length; i++) {
        let j = Math.floor(Math.random() * cardSet.length); //get random index
        //swap
        let temp = cardSet[i];
        cardSet[i] = cardSet[j];
        cardSet[j] = temp;
    }
}

function startGame() {
    //arrange the board 4x5
    for (let r = 0; r < rows; r++) {
        let row = [];
        for (let c = 0; c < columns; c++) {
            let cardImg = cardSet.pop();

            let card = document.createElement("div");
            card.id = r.toString() + "-" + c.toString();
            card.classList.add("card");
            card.dataset.cardType = cardImg; // Store card type as data attribute
            card.addEventListener("click", selectCard);
            document.getElementById("board").append(card);

        }
        board.push(row);
    }
    setTimeout(hideCards, 1000);
}

function hideCards() {
    var cards = document.querySelectorAll('.card');
    cards.forEach(function(card) {
        card.style.backgroundImage = "url('/static/images/back.jpg')";
    });
}

function selectCard() {
    if (lockBoard || this.classList.contains("matched")) return; // Do not allow selection on matched or locked cards
    if (!this.classList.contains("flip")) {
        this.style.backgroundImage = "url('/static/images/" + this.dataset.cardType + ".jpg')"; // Flip the card
        this.classList.add("flip");
        if (!card1Selected) {
            card1Selected = this;
        } else if (!card2Selected && this != card1Selected) {
            card2Selected = this;
            checkForMatch();
        }
    }
}

function checkForMatch() {
    if (card1Selected.dataset.cardType === card2Selected.dataset.cardType) {
        card1Selected.classList.add("matched");
        card2Selected.classList.add("matched");
        card1Selected = null;
        card2Selected = null;
        checkForWin();
    } else {
        lockBoard = true; // Lock the board to prevent flipping other cards
        setTimeout(() => {
            card1Selected.style.backgroundImage = "url('/static/images/back.jpg')"; // Flip back the cards
            card2Selected.style.backgroundImage = "url('/static/images/back.jpg')";
            card1Selected.classList.remove("flip");
            card2Selected.classList.remove("flip");
            card1Selected = null;
            card2Selected = null;
            lockBoard = false; // Unlock the board after flipping back
            errors += 1;
            document.getElementById("errors").innerText = errors;
        }, 1000);
    }
}


function checkForWin() {
    var matchedCards = document.querySelectorAll('.card.matched');
    if (matchedCards.length === rows * columns) {
        displayCongratulations();
    }
}

function displayCongratulations() {
    var congratulationsMsg = document.createElement("div");
    congratulationsMsg.classList.add("congratulations");
    congratulationsMsg.innerText = "Congratulations! You've matched all the cards!";
    document.body.appendChild(congratulationsMsg);

    // Call createConfetti immediately
    createConfetti();

    // Call createConfetti every 100 milliseconds
    confettiInterval = setInterval(createConfetti, 100);
}



function createConfetti() {
    var confetti = document.createElement("div");
    confetti.classList.add("confetti");
    var randomColor = "#" + Math.floor(Math.random() * 16777215).toString(16); // Generate random color
    confetti.style.backgroundColor = randomColor;
    var randomPositionX = Math.random() * window.innerWidth; // Random X position
    var randomPositionY = -10; // Start confetti above the screen
    confetti.style.left = randomPositionX + "px";
    confetti.style.top = randomPositionY + "px";
    document.body.appendChild(confetti);

    // Animation to make confetti fall
    setTimeout(() => {
        confetti.style.transition = "top 5s ease"; // Adjust duration to control falling speed
        confetti.style.top = window.innerHeight + "px";
        confetti.addEventListener("transitionend", function() {
            this.remove(); // Remove confetti after animation ends
        });
    }, 100);
}

