# VaultClue - The Bagels Number Guessing Game

<!-- ![VaultClue](link-to-your-game-screenshot.png) -->

## Table of Contents

- [Introduction](#introduction)
- [Rules and Gameplay](#rules-and-gameplay)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Clues](#game-clues)


## Introduction

**Deep within the heart of a secret underground facility,** a new vault has just arrived, and it's unlike any vault you've ever encountered before. This vault goes by the enigmatic name "VaultClue," and it holds a tantalizing mystery. What sets VaultClue apart is that it has no password, no traditional locks, but rather operates on a cryptic concept known as "Bagels."

The legend surrounding VaultClue tells of an ancient game of deduction, passed down through the ages. In this game, the player must unravel the secret three-digit number held within the vault, a number with no repeating digits. The vault's enigmatic computer generates this elusive number, and your mission, should you choose to accept it, is to decipher it and gain access to the vault's hidden treasures.

## Rules and Gameplay

Bagels is a deduction game where you must guess the secret three-digit number. After each guess, the computer provides you with three types of clues:

- **Bagels:** None of the three digits guessed is in the secret number.
- **Pico:** One of the digits is in the secret number, but in the wrong place.
- **Fermi:** The guess has a correct digit in the correct place.

**Password Change Mechanism:**
Beware! The vault is cunning, and it's programmed to adapt. After 10 consecutive incorrect guesses, the vault will change its secret number, making your mission even more challenging. Stay sharp and focused, as you have a limited number of attempts to unlock its mysteries!

The computer can give multiple clues, which are sorted in random order. For example, if the secret number is 456 and your guess is 546, the clues could be "fermi pico pico" or "pico fermi pico," indicating 'fermi' from 6 and 'pico pico' from 4 & 5.

## Getting Started

Follow these steps to start your mission to open the VaultClue:

### Prerequisites

- Python 3.x installed on your system.
- Kivy library.

### How to play

1. Launch the game by executing main.py.
2. The mysterious computer within VaultClue will conjure a secret three-digit number, hidden deep within its vaulted chambers.
3. Enter your own guess for this elusive number using the on-screen interface.
4. After each guess, the computer will provide you with its cryptic clues, guiding your path to revelation.
5. Continue your quest to unravel the secrets within the vault until you triumphantly unlock its treasures!
