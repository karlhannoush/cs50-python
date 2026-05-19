def main():
    time = input("What time is it? ")
    if 7 <= convert(time) <= 8:
        print("Breakfast time!")
    elif 12 <= convert(time) <= 13:
        print("Lunch time!")
    elif 18 <= convert(time) <= 19:
        print("Dinner time!")

def convert(time):
    time_list = time.split(":")
    hour = float(time_list[0].strip())
    minute = float(time_list[1].strip())
    return hour + minute/60

main()