def main():
    menu = (
        "===STUDENT UTILITY TOOLKIT===\n\n"
        "1. Course Average Calculator\n"
        "2. Passing grade Calculator\n"
        "3. GPA Calculator\n"
        "4. Exit\n\n")
    
    user = "1"
    while user in ['1','2','3']:
        user = input(menu)
        if user == "1":
            avg_calculator()
        elif user == "2":
            pass_calculator()
        elif user == "3":
            gpa_calculator()
        elif user != "4":
            print("\nChoose between 1 and 3\n\n")


def avg_calculator():
    while True: 
        try:
            grade_nb = int(input("How many grades do you currently know? "))
        except ValueError:
            print("\nEnter a number\n")
        else:
            if grade_nb <= 0:
                print("\nEnter a valid number\n")
            else:
                break
    grade_dic = {}
    weight_sum = 0
    i = 0
    while weight_sum <= 1 and i < grade_nb:
        while True:
            try:
                grade_dic[i] = float(input(f"Grade {i+1}: "))
            except ValueError:
                print("\nEnter a valid grade\n")
            else:
                if not 0 <= grade_dic[i] <= 20:
                    print("\nEnter a grade between 0 and 20\n")
                else:
                    break
        while True:
            try:
                inp = input(f"Weight of grade {i+1}: ")
                grade_dic[grade_dic[i]] = float(inp)
            except ValueError:
                try:
                    percent = float(inp.replace("%",""))
                except ValueError:
                    print("\nEnter a percentage (0%-100%) or a decimal (0-1)\n")
                else:
                    if 0 <= percent <= 100:
                        grade_dic[grade_dic[i]] = percent/100
                        weight_sum += grade_dic[grade_dic[i]]
                        break
                    else:
                        print("\nEnter a percentage (0%-100%) or a decimal (0-1)\n")
            else:
                if not 0 <= grade_dic[grade_dic[i]] <= 1:
                    print("\nEnter a percentage (0%-100%) or a decimal (0-1)\n")
                else:
                    weight_sum += grade_dic[grade_dic[i]]
                    break
        i += 1        
    if weight_sum > 1:
        print("\nSum of weights can't exceed 1 or 100%\n")
    else:
        avg = 0
        try:
            for i in range(grade_nb):
                avg += grade_dic[i]*(grade_dic[grade_dic[i]]/weight_sum)
        except ZeroDivisionError:
            print("\nWeights can't all be 0\n")
        else:
            if weight_sum == 1:
                print(f"\nYour course final average is {avg:.2f}/20\n")
            else:
                print(f"\nYour course average currently is {avg:.2f}/20\n")

def pass_calculator():
    
    while True: 
        try:
            grade_nb = int(input("How many grades do you currently know? "))
        except ValueError:
            print("\nEnter a number\n")
        else:
            if grade_nb <= 0:
                print("\nEnter a valid number\n")
            else:
                break
    grade_dic = {}
    weight_sum = 0
    i = 0
    while weight_sum < 1 and i < grade_nb:
        while True:
            try:
                grade_dic[i] = float(input(f"Grade {i+1}: "))
            except ValueError:
                print("\nEnter a valid grade\n")
            else:
                if not 0 <= grade_dic[i] <= 20:
                    print("\nEnter a grade between 0 and 20\n")
                else:
                    break
        while True:
            try:
                inp = input(f"Weight of grade {i+1}: ")
                grade_dic[grade_dic[i]] = float(inp)
            except ValueError:
                try:
                    percent = float(inp.replace("%",""))
                except ValueError:
                    print("\nEnter a percentage (0%-100%) or a decimal (0-1)\n")
                else:
                    if 0 <= percent <= 100:
                        grade_dic[grade_dic[i]] = percent/100
                        weight_sum += grade_dic[grade_dic[i]]
                        break
                    else:
                        print("\nEnter a percentage (0%-100%) or a decimal (0-1)\n")
            else:
                if not 0 <= grade_dic[grade_dic[i]] <= 1:
                    print("\nEnter a percentage (0%-100%) or a decimal (0-1)\n")
                else:
                    weight_sum += grade_dic[grade_dic[i]]
                    break
        i += 1        
    if weight_sum >= 1:
        print("\nSum of weights must be less than 1 or 100%\n")
    else:
        while True:
            try:
                avg = float(input("What average do you need to pass? "))
            except ValueError:
                print("\nEnter a valid average\n")
            else:
                if 0 <= avg <= 20:
                    grd = avg
                    grd_weight = 1
                    for i in range(grade_nb):
                        grd -= grade_dic[i]*grade_dic[grade_dic[i]]
                        grd_weight -= grade_dic[grade_dic[i]]
                    final = grd/grd_weight
                    if final <=0:
                        print("\nYou don't need any marks on the final to pass\n")
                        break
                    elif 0 < final < 20:
                        print(f"\nYou need to get {final:.2f}/20 on the final to pass\n")
                        break
                    else:
                        print("\nDon't go to the final, you failed\n")
                        break
                else:
                    print("\nEnter an average between 0 and 20\n")

def gpa_calculator():
    while True:
        try:
            course_nb = int(input("How many courses do you have? "))
        except ValueError:
            print("\nEnter a number\n")
        else:
            if course_nb <= 0:
                print("\nEnter a valid number\n")
            else:
                break

    total_credits = 0
    course_list = []
    for k in range(course_nb):
        dic_course = {"Credits":0,"Average":0}
        print(f"\n== Course {k+1} ==")
        while True:
            try:
                credits = int(input("Number of credits: "))
            except ValueError:
                print("\nEnter an integer\n")
            else:
                if credits <=0:
                    print("\nEnter a valid integer\n")
                else:
                    total_credits += credits
                    dic_course["Credits"] = credits
                    break


        while True: 
            try:
                grade_nb = int(input("How many grades do you currently know? "))
            except ValueError:
                print("\nEnter a number\n")
            else:
                if grade_nb <= 0:
                    print("\nEnter a valid number\n")
                else:
                    break

        grade_dic = {}
        weight_sum = 0
        i = 0
        while weight_sum <= 1 and i < grade_nb:
            while True:
                try:
                    grade_dic[i] = float(input(f"Grade {i+1}: "))
                except ValueError:
                    print("\nEnter a valid grade\n")
                else:
                    if not 0 <= grade_dic[i] <= 20:
                        print("\nEnter a grade between 0 and 20\n")
                    else:
                        break
            while True:
                try:
                    inp = input(f"Weight of grade {i+1}: ")
                    grade_dic[grade_dic[i]] = float(inp)
                except ValueError:
                    try:
                        percent = float(inp.replace("%",""))
                    except ValueError:
                        print("\nEnter a percentage (0%-100%) or a decimal (0-1)\n")
                    else:
                        if 0 <= percent <= 100:
                            grade_dic[grade_dic[i]] = percent/100
                            weight_sum += grade_dic[grade_dic[i]]
                            break
                        else:
                            print("\nEnter a percentage (0%-100%) or a decimal (0-1)\n")
                else:
                    if not 0 <= grade_dic[grade_dic[i]] <= 1:
                        print("\nEnter a percentage (0%-100%) or a decimal (0-1)\n")
                    else:
                        weight_sum += grade_dic[grade_dic[i]]
                        break
            i += 1        

        if weight_sum > 1:
            print("\nSum of weights can't exceed 1 or 100%\n")
        else:
            avg = 0
            try:
                for i in range(grade_nb):
                    avg += grade_dic[i]*(grade_dic[grade_dic[i]]/weight_sum)
            except ZeroDivisionError:
                print("Weights can't all be 0\n")
            else:
                dic_course["Average"] = avg
                course_list.append(dic_course)
    
    gpa = 0
    for dic in course_list:
        gpa += dic["Average"]*dic["Credits"]/total_credits

    print(f"Your GPA is {gpa:.2f}/20\n")

main()
