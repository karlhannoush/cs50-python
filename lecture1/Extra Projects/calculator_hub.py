def main():
    menu = (
    "=== Calculator Hub ===\n\n"
    "1. Basic Calculator\n"
    "2. Ohm's law Calculator\n"
    "3. BMI Calculator\n"
    "4. Temperature Converter\n"
    "5. Exit\n\n")
    
    user = "1"
    while user in ['1','2','3','4']:
        print()
        user = input(menu)
        if user == "1":
            calculate()
        elif user == "2":
            ohm()
        elif user == "3":
            bmi()
        elif user == "4":
            temp()
        else:
            if user != "5":
                print("Choose between 1 and 5\n")
        

def calculate():
    print()
    expression = input("Expression (with spaces between the characters): ")
    space_indx = expression.find(" ")
    operation = expression[space_indx +1]

    expression_list = expression.split(operation)
    x = int(expression_list[0].strip())
    z = int(expression_list[1].strip())

    if operation == "+":
        result = round(float(x + z),2)
    elif operation == "-":
        result = round(float(x - z),2)
    elif operation == "*":
        result = round(float(x * z),2)
    elif operation == "/":
        if z == 0:
            result = "Undefined"
        else:
            result = round(float(x / z),2)

    print(result)    


def ohm():
    print()
    menu = (
    "What do you want to calculate?\n"
    "1. U\n"
    "2. R\n"
    "3. I\n\n")
    info = " "
    
    while info not in ['1','2','3']:
        info = input(menu)
        if info not in ['1','2','3']:
            print("Choose 1,2 or 3\n")
        
    U,R,I = -1,-1,-1
    if info == "1":
        while R < 0:
            R = float(input("R: "))
            if R < 0:
                print("Resistance must be non-negative\n")
        while I < 0:
            I = float(input("I: "))
            if I < 0:
                print("Current must be non-negative\n")
        print(f"U = {round(R*I,2)}V")
    elif info == "2":
        while U < 0:
            U = float(input("U: "))
            if U < 0:
                print("Voltage must be non-negative\n")
        while I <= 0:    
            I = float(input("I: "))
            if I <= 0:
                print("Current must be positive\n")
        print(f"R = {round(U/I,2)}Ω")
    elif info == "3":
        while U < 0:    
            U = float(input("U: "))
            if U < 0:
                print("Voltage must be non-negative\n")
        while R <= 0:    
            R = float(input("R: "))
            if R <= 0:
                print("Resistance must be positive\n")
        print(f"I = {round(U/R,2)}A")


def bmi():
    print()
    units = " "
    menu = (
    "What units do you use?\n"
    "1. Metric\n"
    "2. Imperial\n\n")
    while units not in ['1','2']:
        units = input(menu)
        if units not in ['1','2']:
            print("Choose 1 or 2\n")

    if units == "1":
        weight_kg,height_cm = -1,-1
        while weight_kg <= 0:
            weight_kg = float(input("What's your weight in kg? "))
            if weight_kg <= 0:
                print("Weight must be positive\n")

        while height_cm <= 0:
            height_cm = float(input("What's your height in cm? "))
            if height_cm <= 0:
                print("Height must be positive\n")
        height_m = height_cm/100

    elif units == "2":
        weight_lb = -1
        while weight_lb <= 0:
            weight_lb = float(input("What's your weight in lb? "))
            if weight_lb <= 0:
                print("Weight must be positive\n")
        weight_kg = round(weight_lb/2.20462 , 2)

        feet,inches = -1,-1
        while (feet < 0 or inches < 0) or (feet == 0 and inches == 0):
            height_ft_inch = input("What's your height in ft? ")
            height_ft_inch_list1 = height_ft_inch.split("'")
            feet = int(height_ft_inch_list1[0])
            if height_ft_inch.strip().endswith('"'):
                inches = int(height_ft_inch_list1[1].replace('"',''))
            else:
                inches = 0
            if (feet < 0 or inches < 0) or (feet == 0 and inches == 0):
                if feet < 0 and inches >=0:
                    print("Feet can't be negative\n")
                elif feet >= 0 and inches < 0:
                    print("Inches can't be negative\n")
                elif feet < 0 and inches < 0:
                    print("Feet and inches can't be negative\n")
                elif feet == 0 and inches == 0:
                    print("Height must be positive\n")
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


def temp():
    print()
    min_C = -273.15
    min_F = -459.67
    min_K = 0
    value = -1000
    units = " "
    menu = (
    "From what unit do you want to convert?\n"
    "1. °C\n"
    "2. °F\n"
    "3. K\n\n")

    while units not in ['1','2','3']:
        units = input(menu)
        if units not in ['1','2','3']:
            print("Choose 1, 2 or 3\n")

    units_to = " "
    if units == "1":
        menu_to = (
            "To what unit?\n"
            "1. °F\n"
            "2. K\n\n")
  
        while units_to not in ['1','2']:
            units_to = input(menu_to)
            if units_to not in ['1','2']:
                print("Choose 1 or 2\n")

        while value < min_C:
            value = float(input("How many °C? "))
            if value < min_C:
                print("Temperature must be greater or equal than -273.15 °C\n")
        
        if units_to == "1":
            result = value*1.8 + 32
            print(f"{round(result,2)} °F")
        elif units_to == "2":
            result = value + 273.15
            print(f"{round(result,2)} K")
         

    elif units == "2":
        menu_to = (
            "To what unit?\n"
            "1. °C\n"
            "2. K\n\n")

        while units_to not in ['1','2']:
            units_to = input(menu_to)
            if units_to not in ['1','2']:
                print("Choose 1 or 2\n")
       
        while value < min_F:
            value = float(input("How many °F? "))
            if value < min_F:
                print("Temperature must be greater or equal to -459.67 °F\n")

        if units_to == "1":
            result = (value -32)/1.8
            print(f"{round(result,2)} °C")
        elif units_to == "2":
            result = (value - 32)/1.8 + 273.15
            print(f"{round(result,2)} K")

    elif units == "3":
        menu_to = (
            "To what unit?\n"
            "1. °C\n"
            "2. °F\n\n")

        while units_to not in ['1','2']:
            units_to = input(menu_to)
            if units_to not in ['1','2']:
                print("Choose 1 or 2\n")
          
        while value < min_K:
            value = float(input("How many K? "))
            if value < min_K:
                print("Temperature must be greater or equal to 0 K\n")


        if units_to == "1":
            result = value -273.15
            print(f"{round(result,2)} °C")
        elif units_to == "2":
            result = (value - 273.15)*1.8 +32
            print(f"{round(result,2)}") 



main()
