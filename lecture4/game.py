def main():
    from random import randint


    rand_int = randint(1,get_int())

    user = -1
    while user <= 0 or user != rand_int:
        try:
            user = int(input("Guess: "))
        except ValueError:
            print("Enter an integer")
        else:
            if 0 < user < rand_int:
                print("Too small!")
            elif user > rand_int:
                print("Too large!")
            elif user == rand_int:
                print("Just right!")


def get_int():

    while True:
        try:
            n = int(input("n: "))
        except ValueError:
            print("Enter an integer")
        else:
            if n <= 0:
                print("Enter a positive integer")
            else:
                return n
            
main()