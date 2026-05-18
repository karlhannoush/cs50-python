def main():
    meal = input("How much was the meal? ")
    tip = input("How much would you like to tip? ")
    meal_fl = DollarsToFloat(meal)
    tip_fl = PercentToFloat(tip)
    amount = meal_fl*tip_fl
    print(f"You must tip ${round(amount,2)}")

def DollarsToFloat(money):
    money_list = money.split("$")
    return(float(money_list[1]))

def PercentToFloat(percent):
    percent_list = percent.split("%")
    return float(percent_list[0])/100

main()