Lecture 3 — Exceptions

This lecture focused on handling invalid input and making programs more robust using try, except, and validation loops.

Compared to the previous lectures, the problems started requiring much more defensive programming. Instead of only making programs work for ideal input, I had to think about incorrect formats, impossible values, edge cases, and repeated prompting until the user enters valid data.

I also started working with:

dictionaries more heavily,
reusable validation functions,
structured input parsing,
and Python libraries like datetime.
Problem Set
Fuel Gauge

A program that:

accepts fractions like 3/4,
converts them into percentages,
handles invalid input using exceptions,
and displays:
E for empty,
F for full,
or the percentage otherwise.

Concepts practiced:

try / except
nested validation
loops
numeric conversion
edge-case handling
Grocery List

A grocery list tracker that:

continuously accepts items from the user,
counts repetitions,
and prints the results alphabetically in uppercase after input ends.

Concepts practiced:

dictionaries
counting occurrences
infinite loops
handling keyboard interruption
Felipe’s Taqueria

A restaurant ordering system that:

accepts menu items,
ignores invalid entries,
and continuously updates the running total.

Concepts practiced:

dictionaries
string normalization
cumulative totals
input validation
Outdated

A date conversion program that:

accepts multiple date formats,
validates user input,
and converts dates into ISO format (YYYY-MM-DD).

This was the hardest problem of the lecture for me because it required:

parsing different input formats,
validating dates,
handling multiple exception types,
and correctly passing values between functions.

Concepts practiced:

complex validation logic
tuples and argument unpacking
formatting with f-strings
exception handling
reusable helper functions
Extra Projects
Age Calculator

A program that:

asks for a birth date,
validates leap years and calendar rules,
and calculates age using Python’s datetime module.

This was my first time using the datetime library.

Concepts practiced:

importing libraries
date arithmetic
leap year validation
structured validation logic
Student Utility Toolkit

A larger multi-function project containing:

course average calculator,
passing-grade calculator,
GPA calculator.

This project focused heavily on:

validation,
exception handling,
weighted averages,
nested loops,
dictionaries,
and organizing larger programs into multiple functions.

The project became significantly longer than my previous projects (~260 lines), and it exposed weaknesses in my code structure and repetition. But it also forced me to think more carefully about program organization and reusable logic.
