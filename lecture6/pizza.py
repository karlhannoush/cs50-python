import sys
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Enter a CSV file")

try:
    with open(sys.argv[1]) as file:
        final_list = []
        for line in file:
            final_list.append(line.split(","))
    print(tabulate(final_list, headers = "firstrow", tablefmt = "grid"))
except FileNotFoundError:
    sys.exit("File not found. Please try again")
