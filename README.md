# Character-Guessing-Game
An interactive, fandom-fueled Python Word Guessing Game that challenges players to identify iconic Marvel or DC characters before they run out of attempts!

🦸‍♂️ Superhero Word Guessing Game
Welcome to the ultimate test of cinematic knowledge! This Superhero Word Guessing Game is a Python-powered adventure that brings the rivalry between Marvel and DC to your terminal. Whether you're a fan of the MCU or the DCU, this game adapts to your preference and challenges you to save the day one letter at a time!

🌟 Features
Choose Your Universe: A dynamic branching system that changes the word bank based on your allegiance (Marvel vs. DC).

Intelligent Gameplay Engine: Handles multi-word names (like Captain America) by automatically displaying spaces, ensuring a smooth user experience.

Real-time Progress Tracking: Visual feedback using underscores and revealed letters to keep the tension high.

Customized Experience: Greets players by name and provides tailored feedback based on their movie tastes.

🛠️ How It Works
The project utilizes core programming concepts to create a seamless loop:

Input & Personalization: The program captures your name and your favorite universe using the input() function.

Conditional Logic: Using if-elif-else statements, the game selects a specific list of characters. If you choose "Marvel," you won't get "Batman"!

The Game Loop: A while loop runs the logic, checking if you still have "turns" (lives) left.

Letter Validation: A nested for loop iterates through the secret word to check if your guessed letter matches any character in the name.

🧠 Logic Breakdown
The game is built on the DRY (Don't Repeat Yourself) principle. Rather than writing three separate games, the script dynamically assigns the words variable and runs a universal "Game Engine" loop at the end. This makes the code efficient, readable, and easy to expand!
