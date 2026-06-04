# Lecture 4 – Libraries

This folder contains my solutions and practice projects for Lecture 4 of CS50P, which introduced Python libraries.

Compared to the previous lectures, this one felt like a major step forward. Instead of only writing code with built-in Python features, I started working with external modules, command-line arguments, randomness, dates, APIs, JSON data, and HTTP requests. It was also the first lecture where I had to spend significant time reading documentation and figuring out how libraries are meant to be used.

## Topics Covered

* Importing modules
* Command-line arguments (`sys`)
* Random number generation (`random`)
* Working with dates and times (`datetime`)
* External Python packages
* API requests with `requests`
* JSON data
* Reading library documentation

## Problem Set

### Emojize

Converts emoji aliases such as `:thumbs_up:` into actual emoji characters using the `emoji` library.

### Figlet

Generates ASCII art text using the `pyfiglet` library. This exercise required handling command-line arguments and validating font names. Finding the list of available fonts took some investigation into the library's documentation and functions.

### Adieu, Adieu

Collects names from the user and prints a farewell message using proper English list formatting.

### Guessing Game

Generates a random number and asks the user to guess it while providing feedback after each attempt.

### Little Professor

Creates ten randomly generated math problems and tracks the user's score while handling invalid inputs and multiple attempts.

### Bitcoin Price Index

I was unable to complete this exercise because the API service required an account and API key, and I could not complete the account verification process. However, I still spent time studying how APIs, requests, and JSON responses work, since those concepts seemed particularly important.

## Additional Practice Project:

### Cryptocurrency Price Calculator

I built this project as a replacement for the Bitcoin exercise.

The program:

* Accepts a cryptocurrency name
* Retrieves live pricing data from the CoinGecko API
* Parses JSON responses
* Calculates the value of any amount entered by the user

This was my first project that consumed real-time data from an online API. More importantly, it forced me to learn how to:

* Read API documentation
* Send HTTP requests
* Inspect JSON responses
* Extract nested values from dictionaries
* Handle request and input errors
