# 📘 Assignment: Games in Python

## 🎯 Objective

Create a playable text-based game in Python that practices using strings, loops, conditionals, and user input through a classic word-guessing challenge.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Write a Python program that lets the player guess letters in a hidden word before running out of attempts.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list of words
- Display the hidden word as underscores or blanks for each letter
- Accept one letter guess at a time from the player
- Reveal correctly guessed letters in the word
- Track incorrect guesses and remaining attempts
- End the game when the word is fully guessed or the player runs out of turns
- Print a clear win or lose message at the end

### 🛠️ Add Game Flow and Feedback

#### Description
Improve the game so it feels polished and easy to play by adding clear feedback after each guess and allowing repeated rounds.

#### Requirements
Completed program should:

- Show the current word progress after every guess
- Inform the player when a letter is already guessed
- Keep track of wrong guesses and display them to the user
- Ask whether the player wants to play again after the round ends
- Use readable terminal output with simple, consistent formatting
- Example output:
  ```python
  Word: _ _ _ _ _
  Guess a letter: a
  Correct! You have 6 guesses left.
  ```
