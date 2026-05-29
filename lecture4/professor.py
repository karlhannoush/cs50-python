import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        tries = 3
        (x,y) = (generate_integer(level),generate_integer(level))
        problem = x + y
        solution = int(x + y)
        user = -1
        while tries > 0 and user != solution:
            try:
                user = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                tries -= 1
            else:
                if user != solution:
                    print("EEE")
                    tries -= 1
        if tries == 0:
            print(f"{x} + {y} = {solution}")
        else:
            score += 1
    print(f"Your score is {score}/10")




def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            print("Enter an integer")
        else:
            if n not in [1,2,3]:
                print("Choose a level between 1 and 3")
            else:
                return n

def generate_integer(level):
    if level == 1:
        n = random.randint(0,9)
    elif level == 2:
        n = random.randint(10,99)
    else:
        n = random.randint(100,999)
    return n


if __name__ == "__main__":
    main()