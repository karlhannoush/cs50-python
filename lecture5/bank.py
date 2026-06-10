def main():
    greeting = input("greeting: ").strip().lower()
    number = value(greeting)
    if number == 0:
        print("You get $0")
    elif number == 20:
        print("You get $20")
    elif number == 100:
        print("You get $100")     



def value(greeting):
    if greeting.startswith("h"):
        if greeting.startswith("hello"):
            return 0
        else:
            return 20
    else:
        return 100
    

if __name__ == "__main__":
    main()