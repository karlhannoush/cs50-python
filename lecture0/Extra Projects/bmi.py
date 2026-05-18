units = " "
while units.lower() != "metric" and units.lower() != "imperial":
    units = input("What units do you use? Metric or Imperial? ")

if units.lower() == "metric":
    weight_kg = float(input("What's your weight in kg? "))
    height_cm = int(input("What's your height in cm? "))
    height_m = height_cm/100

elif units.lower() == "imperial":
    weight_lb = float(input("What's your weight in lb? "))
    height_ft_inch = input("What's your height in ft? ")
    weight_kg = round(weight_lb/2.20462 , 2)
    height_ft_inch_list1 = height_ft_inch.split("'")
    feet = int(height_ft_inch_list1[0])
    inches = int(height_ft_inch_list1[1].replace('"',''))
    height_m = round(feet*12*2.54 + inches*2.54)/100

bmi = round(weight_kg/height_m**2 , 2)

if bmi < 18.5:
    case = "Underweight"
elif 18.5 <= bmi < 25:
    case = "Healthy"
elif 25 <= bmi < 30:
    case = "Overweight"
else:
    case = "Obese"

print(f"Your BMI is {bmi} and you're {case.lower()}")