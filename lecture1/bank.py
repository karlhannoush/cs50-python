greeting = input("greeting: ").strip().lower()

if greeting.startswith("h"):
    if greeting.startswith("hello"):
        print("You get $0")
    else:
        print("You get $20")
else:
    print("You get $100")