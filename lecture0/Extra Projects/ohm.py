info = " "
while info.upper() != "I" and info.upper() != "R" and info.upper() != "U":
    info = input("What do you want to calculate? U or R or I? ")

if info.upper() == "U":
    R = float(input("What's R? "))
    I = float(input("What's I? "))
    print(f"U = {round(R*I,2)}")
elif info.upper() == "R":
    U = float(input("What's U? "))
    I = float(input("What's I? "))
    print(f"R = {round(U/I,2)}")
elif info.upper() == "I":
    U = float(input("What's U? "))
    R = float(input("What's R? "))
    print(f"I = {round(U/R,2)}")
