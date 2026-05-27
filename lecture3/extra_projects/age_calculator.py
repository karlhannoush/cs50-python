def main():
    from datetime import date
    from math import floor
    today = date.today()
    birthday = date(*valid_date())
    difference = (today - birthday).days
    age = difference/365.25
    print(f"You're {floor(age)} years old\n")

def valid_date():
    while True:
        birthday = input("Enter your birthday (day/month/year): ")
        try:
            day = int(birthday.split("/")[0])
            month = int(birthday.split("/")[1])
            year = int(birthday.split("/")[2])
        except (ValueError,IndexError):
            print("Invalid date")
        else:
            if year%4 == 0:
                if year%100 == 0:
                    if year%400 == 0:
                        Leap = True
                    else:
                        Leap = False
                else:
                    Leap = True
            else:
                Leap = False
            
            thirty_days = [9,4,6,11]
            if month in thirty_days and not 1<= day <= 30:
                print("Invalid date")
            elif month not in thirty_days and month!=2 and not 1<= day <= 31:
                print("Invalid date")
            elif month == 2 and Leap == True and not 1<= day <= 29:
                print("Invalid date")
            elif month == 2 and Leap == False and not 1<= day <= 28:
                print("Invalid date")
            else:
                return year, month, day
            
main()