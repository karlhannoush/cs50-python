import csv
import datetime

def main():
    main_menu = (
        "=== STUDY LOGGER ===\n\n"
        "1. Log Study Session\n"
        "2. View Today's Total\n"
        "3. View Last 7 Days Total\n"
        "4. Exit\n\n"
    )
    user = "1"
    while user in ['1','2','3']:
        user = input(main_menu)
        if user == "1":
            log_session()
        elif user == "2":
            today()
        elif user == "3":
            last_7_days()
        elif user != "4":
            print("Please choose between 1 and 4\n")

def log_session():
    with open("study_log.csv") as file:
                first_line = file.readline()
    with open("study_log.csv","a",newline = "") as file:
        writer = csv.DictWriter(file, fieldnames = ["date","subject","duration"])
        today = datetime.date.today()
        if first_line.strip() != "date,subject,duration":
            writer.writeheader()
        writer.writerow({"date":today,"subject":get_subject(),"duration":get_duration()})

def get_subject():
    return input("Subject: ").strip().title()

def get_duration():
    while True:
        try:
            duration = int(input("Duration (mins): "))
        except ValueError:
            print("Enter a number of minutes")
        else:
            if duration > 0:
                return duration
            else:
                print("Enter a positive duration\n\n")

def today():
    count = 0
    today = datetime.date.today()
    with open("study_log.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["date"] == str(today):
                count += int(row["duration"])
    print(f"You studied for {count} minutes today")

def last_7_days():
    count = 0
    list_7_days = []
    for i in range(7):
        list_7_days.append(str(datetime.date.today() - datetime.timedelta(days=i)))
    with open ("study_log.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["date"] in list_7_days:
                count += int(row["duration"])
    print(f"You studied for {count} minutes in the last 7 days")

if __name__ == "__main__":
     main()