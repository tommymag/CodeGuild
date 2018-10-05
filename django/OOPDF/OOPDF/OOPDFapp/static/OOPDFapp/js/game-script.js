let flashcards = []
let question = document.querySelector('#question')
let aSelectBtn = document.querySelector('#a-select-btn')
let bSelectBtn = document.querySelector('#b-select-btn')
let cSelectBtn = document.querySelector('#c-select-btn')
let dSelectBtn = document.querySelector('#d-select-btn')
let choices = []
let questionsleft = 14
let wrongAnswers = 0
let currentCard = 0
let isTerm = true

fetch('http://localhost:8000/flashcards/')
	.then(response => {
		console.log(response)
		return response.json()
	})
	.catch(errors => {
		console.log(errors)
	})
	.then(responseJson => {
		flashcards = JSON.parse(responseJson)
		askQuestion()
		document.getElementById('select-btn-a').addEventListener('click', () => {
			checkAnswer(choices[0])
		})
		document.getElementById('select-btn-b').addEventListener('click', () => {
			checkAnswer(choices[1])
		})
		document.getElementById('select-btn-c').addEventListener('click', () => {
			checkAnswer(choices[2])
		})
		document.getElementById('select-btn-d').addEventListener('click', () => {
			checkAnswer(choices[3])
		})
	})	




function questionTerm(flashcard) {
	let termElement = document.createElement('p')
	termElement.innerText = flashcard.fields.term 
	question.appendChild(termElement)
}

function populateChoicesA(flashcard) {
	let definitionElement = document.createElement('p')
	definitionElement.innerText = 'A: ' + flashcard.fields.definition 
	question.appendChild(definitionElement)	
}

function populateChoicesB(flashcard){
	let definitionElement = document.createElement('p')
	definitionElement.innerText = 'B: ' + flashcard.fields.definition
	question.appendChild(definitionElement)
}

function populateChoicesC(flashcard){
	let definitionElement = document.createElement('p')
	definitionElement.innerText = 'C: ' + flashcard.fields.definition
	question.appendChild(definitionElement)
}

function populateChoicesD(flashcard){
	let definitionElement = document.createElement('p')
	definitionElement.innerText = 'D: ' + flashcard.fields.definition
	question.appendChild(definitionElement)
}

function ofRandSelect(flashcards){
  
return flashcards[Math.floor(Math.random()*flashcards.length)];
     
}

function checkAnswer(choice) {
	let answer = flashcards[currentCard]
	if (answer != choice) {
		thatIsWrong()
	}

	nextQuestion()
}

function askQuestion() {
	questionsleft--
	if (questionsleft == 0){
		gameOver(win=true)
	}
	questionTerm(flashcards[currentCard])
	choices = [flashcards[currentCard]]
	for (let i=0; i<3; i++) {
		let choice = ofRandSelect(flashcards)
		while (choices.includes(choice)) {
			choice = ofRandSelect(flashcards)
		}
		choices.push(choice)
	}

	choices.shuffle()
	// console.log(choices[0] == flashcards[currentCard])
	// console.log(choices[1] == flashcards[currentCard])
	populateChoicesA(choices[0])
	populateChoicesB(choices[1])
	populateChoicesC(choices[2])
	populateChoicesD(choices[3])
}

Array.prototype.shuffle = function () {
	let input = this;
	for (let i = input.length-1; i >=0; i--) {
     
        let randomIndex = Math.floor(Math.random()*(i+1)); 
        let itemAtIndex = input[randomIndex]; 
         
        input[randomIndex] = input[i]; 
        input[i] = itemAtIndex;
    }
    return input;
}

function nextQuestion() {
	if (currentCard + 1 < flashcards.length) {
		currentCard++
		question.innerHTML = ''
		askQuestion()
	} else {
		// do something for game over
		
	}

}

function thatIsWrong(){
	wrongAnswers++
	console.log(wrongAnswers)
	if (wrongAnswers == 1){	
		let alertuser = document.querySelector('.startstatus')
		alertuser.style.display = 'none'
		let alertuserI = document.querySelector('.onewrong')
		alertuserI.style.display = 'block'
	}
	else if (wrongAnswers == 2) { 
		let alertuserII = document.querySelector('.onewrong')
		alertuserII.style.display = 'none'
		let alertuserisfading = document.querySelector('.twowrong')
		alertuserisfading.style.display = 'block'
	} else {
		gameOver(win=false)
	}

} 

function gameOver(win) {
	let clearheaders = document.querySelectorAll('.score-headers')
	let gameoverdiv = document.querySelector('.gameover')
	for (let i=0; i<clearheaders.length; i++) {
		clearheaders[i].style.display = 'none'
	}
	let clearterminal = document.querySelector('.terminal')
	clearterminal.style.display = 'none'

	if (!win) {
		let mvgMortem = document.querySelector('.Mortem')
		mvgMortem.style.display = 'block'
	} else {
		gameoverdiv.innerHTML = "<h1 class='present'><span id='logooopdfblue'>OO</span><span id='logooopdfpink'>PDF</span></h1>"
		gameoverdiv.innerHTML = "<div class='youwin'><h2>You Win</h2> <span class='cursor'>|</span></div>"
	}
	
}

// document.getElementById('quit').addEventListener('click', () => {
// 	quitGame()
// 		})

// function quitGame(){

// }


// function questionReveal() {
// 	let flashcard = flashcards[currentCard]
// 	flashcardContainer.innerHTML = ''
// 	if (isTerm) {
// 		backBuild(flashcard)
// 	} else {
// 		frontBuild(flashcard)

// 	}
// 	isTerm = !isTerm
// }

