# Lecture 6 – File I/O


This lecture introduced reading from and writing to files in Python. Topics included:

* Opening and closing files
* Reading text files
* Writing and appending data to files
* CSV files
* The `csv` module
* Command-line arguments with `sys.argv`
* Working with image files using Pillow
* Using third-party libraries for file processing

This lecture felt significantly more practical than previous ones because it focused on storing, loading, and manipulating real data.

---

## Problem Set 6

### Lines of Code

Built a program that counts the number of lines of code in a Python file while ignoring:

* Blank lines
* Comments

Concepts practiced:

* File reading
* Command-line arguments
* String processing
* Error handling

---

### Pizza Py

Built a program that reads a CSV menu and displays it as a formatted table using the `tabulate` library.

Concepts practiced:

* CSV files
* Third-party libraries
* Data formatting

---

### Scourgify

Built a program that cleans and reformats CSV data by splitting names into separate first and last name columns.

Concepts practiced:

* `csv.DictReader`
* `csv.DictWriter`
* Data transformation
* Writing new CSV files

---

### CS50 P-Shirt

Built a program that overlays a transparent shirt image onto another image using the Pillow library.

Concepts practiced:

* Image processing
* `Image.open`
* `ImageOps.fit`
* `Image.paste`
* Saving modified images

This was the most challenging problem of the set and required learning how image objects behave and how transparency masks work.

---

## Project – Study Logger

To reinforce the lecture, I built a Study Logger application that stores study sessions in a CSV file.

Features:

* Log study sessions
* Store date, subject, and duration
* View total study time for today
* View total study time over the last 7 days

Concepts practiced:

* CSV file creation
* CSV reading and writing
* Date handling with `datetime`
* Function decomposition
* Menu-driven applications

The original version grew to more than 300 lines as I experimented with statistics, rankings, percentages, and reporting features. Eventually I simplified the project into a smaller and more maintainable version focused on the core functionality.

This project taught me an important lesson about software development: reducing scope is often better than endlessly adding features.


