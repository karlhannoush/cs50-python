def main():
    x = get_fraction()
    percent = round(x*100)
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")

def get_fraction():
    while True:
        user = input("Fraction: ")
        user_list = user.split("/")
        try:
            x = int(user_list[0])
            y = int(user_list[1])
        except IndexError:
            print("Enter a fraction")
        except ValueError:
            print("Numerator and denominator must be integers")
        
        else:
            try:
                fraction = float(x/y)
            except ZeroDivisionError:
                print("Denominator must be positive")
            else:

                if x > y:
                    print("Fraction must be less than 1")
                elif x < 0 and y >0:
                    print("Numerator must be non negative")
                elif x >= 0 and y <0:
                    print("Denominator must be positive")
                elif x < 0 and y < 0:
                    print("Numerator must be non negative and denominator must be positive")
                else:
                    return fraction
                        

main()