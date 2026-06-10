def main():
    text = input("Your text: ")
    print(no_vowels(text))

def no_vowels(string):
    vowels_str = "aeiou"
    new_str = ""
    for letter in string:
        if letter.lower() not in vowels_str:
            new_str += letter
    return new_str

if __name__ == "__main__":
    main()