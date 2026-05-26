def main():
    print(formatted(*valid_input()))

months_dic = {
        "January":1,
        "February":2,
        "March":3,
        "April":4,
        "May":5,
        "June":6,
        "July":7,
        "August":8,
        "September":9,
        "October":10,
        "November":11,
        "December":12 
    }

def valid_input():
    while True:
        date = input("Date: ")

        try:
            date_list1 = date.split(" ")
            month = date_list1[0]
            day_w_comma = date_list1[1]
            day = int(day_w_comma.replace(",",""))
            year = int(date_list1[2])

        except (ValueError, IndexError):
            try:
                date_list = date.split("/")
                month = int(date_list[0])
                day = int(date_list[1])
                year = int(date_list[2])
            except IndexError:
                print("Enter a date")
            except ValueError:
                print("The month, day and year must be integers")
            else:
                if not (1 <= month <= 12) or not 1 <= day <= 31:
                    if not (1 <= month <= 12):
                        print("Invalid month")
                    if not (1 <= day <= 31):
                        print("Invalid day")
                else:
                    return day,month,year
        else:
            if month not in months_dic or not (1<= day <= 31):
                if month not in months_dic:
                    print("Invalid month")
                if not (1<= day <= 31):
                    print("Invalid day")
            else:
                return day,months_dic[month],year   
    
    

def formatted(day,month,year):
    return f"{year}-{month:02}-{day:02}"
    
main()