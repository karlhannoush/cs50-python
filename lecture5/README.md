# Lecture 5 – Unit Testing

This lecture focused on writing functions that can be tested independently and creating automated tests for them using `pytest`.

Unlike previous lectures, the emphasis was less on building programs and more on verifying that existing code behaves correctly under different inputs.

## Exercises Completed

### Testing my twttr

Reimplemented my vowel-removal program from Lecture 2 and created tests covering:

* Lowercase words
* Uppercase words
* Mixed-case words
* Words containing numbers

### Back to the Bank

Reimplemented the bank greeting program as a reusable function and wrote tests for all possible outcomes:

* Greetings starting with "hello"
* Greetings starting with "h" but not "hello"
* All other greetings

### Re-requesting a Vanity Plate

Reused my vanity plate validator from Lecture 2 and created tests for:

* Valid plates
* Invalid lengths
* Invalid characters
* Invalid number placement
* Invalid starting numbers

## What I Learned

The most important lesson from this lecture was separating program logic from user interaction.

Instead of placing all code inside `main()`, I learned to write functions that return values and can be imported into other files for testing.

I also learned the basics of automated testing with `pytest`, including:

* Writing assertions
* Organizing test files
* Testing edge cases
* Verifying program behavior automatically

