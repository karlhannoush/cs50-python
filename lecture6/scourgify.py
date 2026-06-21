import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many arguments")
elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Enter CSV files")


try:
    with open(sys.argv[1]) as file_before:
        with open(sys.argv[2], "w") as file_after:
            reader = csv.DictReader(file_before)
            writer = csv.DictWriter(file_after, fieldnames = ["first","last","house"])
            writer.writeheader()
            for row in reader:
                name,house = row["name"],row["house"]
                last,first = name.split(",")
                writer.writerow({"first":first.lstrip(), "last":last, "house":house})

except FileNotFoundError:
    sys.exit("File not found, please try again")
            
            