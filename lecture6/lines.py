import sys

if len(sys.argv) == 1:
    sys.exit("specify a file name or path")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Enter a python file")
try:
    with open(sys.argv[1]) as file:
        lines = 0
        for line in file:
            if line.strip() != "" and not line.strip().startswith("#"):
                lines += 1
    print(lines, "lines")
except FileNotFoundError:
    sys.exit("File not found. Please try again")