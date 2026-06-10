def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not length(s):
        return False
    if not no_symb(s):
        return False
    elif not first_2_char(s):
        return False
    elif not nb_end(s):
        return False
    elif not first_number(s):
        return False
    else:
        return True
    
def length(p):
    return 2<=len(p)<=6

def no_symb(p):
    letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    numbers = "0123456789"
    for char in p:
        if char not in letters and char not in numbers:
            return False 
    return True

def first_2_char(p):
    letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    return p[0] in letters and p[1] in letters

def nb_end(p):
    letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    i = 1
    number = False
    while i < len(p) and number == False:
        if p[i] in letters:
            i += 1
        else:
            number = True
    letter = False
    for j in range(i,len(p)):
        if p[j] in letters:
            letter = True
    return not letter

def first_number(p):
    numbers = "0123456789"
    i = 1
    number = False
    while i < len(p) and number == False:
        if p[i] in numbers:
            number = True
        if number == False:
            i +=1
    return p[i] != "0"

if __name__ == "__main__":
    main()