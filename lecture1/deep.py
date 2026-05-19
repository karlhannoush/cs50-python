text = input("The Answer to the Great Question is… ")
edited = text.lower().strip()

if edited == "42" or edited == "forty two" or edited == "forty-two":
    print("Yes")
else:
    print("No")