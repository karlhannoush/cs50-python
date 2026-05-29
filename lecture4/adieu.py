def main():
    names = get_names()
    adieu = "Adieu, adieu, to"
    if len(names) == 1:
         print(adieu, names[0])
    else:
         print(adieu, end = " ")
         for i in range(len(names)):
            if i < len(names)-2:
                print(f"{names[i]},", end = " ")
            elif i == len(names)-2:
                print(f"{names[i]} and", end = " ")
            else:
                print(names[i])

def get_names():
    names = []
    while True:
        try:
            name = str(input("Name: "))
        except ValueError:
            print("Enter a name")
        except KeyboardInterrupt:
            if len(names) == 0:
                print("Enter at least a name")
            else:
                print()
                return names
        else:
            names.append(name.strip())

main()